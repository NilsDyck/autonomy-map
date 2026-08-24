import json
import random
import string
from typing import Dict, List
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Liefert statische Dateien (HTML, CSS, JS) aus dem Ordner "static" aus
app.mount("/static", StaticFiles(directory="static"), name="static")


def generate_room_code() -> str:
    """Generiert einen lesbaren Raumcode wie z. B. MAP-482"""
    digits = "".join(random.choices(string.digits, k=3))
    return f"MAP-{digits}"


def get_default_room_state():
    """Start-Vorlage für eine leere Autonomy Map"""
    return {
        "title": "Neue Autonomy Map",
        "actors": [
            {"id": "act_1", "name": "Nutzer:innen", "perspective": "", "agency": "", "values": ""},
            {"id": "act_2", "name": "Betreiber / Schule", "perspective": "", "agency": "", "values": ""}
        ],
        "options": [
            {"id": "opt_1", "title": "Option A (z. B. Vollautomatisierung)", "implementation": ""},
            {"id": "opt_2", "title": "Option B (z. B. Assistenzsystem)", "implementation": ""}
        ],
        "matrix": {},       # Format: {"opt_1_act_1": {"rating": "+", "comment": "..."}}
        "judgment": ""      # Freitext-Begründung
    }


class RoomManager:
    def __init__(self):
        # Speichert aktive WebSocket-Verbindungen pro Raum
        self.rooms: Dict[str, List[WebSocket]] = {}
        # Speichert den aktuellen Datenzustand pro Raum
        self.data: Dict[str, dict] = {}

    async def connect(self, room_id: str, websocket: WebSocket):
        await websocket.accept()
        if room_id not in self.rooms:
            self.rooms[room_id] = []
            self.data[room_id] = get_default_room_state()
        self.rooms[room_id].append(websocket)
        # Beim Beitreten sofort den aktuellen Stand an den Client schicken
        await websocket.send_json({"type": "INIT_STATE", "data": self.data[room_id]})

    def disconnect(self, room_id: str, websocket: WebSocket):
        if room_id in self.rooms:
            self.rooms[room_id].remove(websocket)

    async def broadcast(self, room_id: str, message: dict, sender: WebSocket):
        # 1. Lokalen Zustand auf dem Server aktualisieren
        msg_type = message.get("type")
        payload = message.get("payload")

        if msg_type == "UPDATE_STATE":
            self.data[room_id] = payload

        # 2. An alle anderen Clients im Raum verteilen
        for connection in self.rooms.get(room_id, []):
            if connection != sender:
                try:
                    await connection.send_json(message)
                except Exception:
                    pass


manager = RoomManager()


@app.get("/")
def serve_index():
    """Startseite ausliefern"""
    return FileResponse("static/index.html")


@app.get("/api/new-room")
def create_room():
    """API-Endpunkt zur Generierung eines neuen Raum-Codes"""
    code = generate_room_code()
    while code in manager.data:
        code = generate_room_code()
    return {"room_id": code}


@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await manager.connect(room_id, websocket)
    try:
        while True:
            text = await websocket.receive_text()
            message = json.loads(text)
            await manager.broadcast(room_id, message, websocket)
    except WebSocketDisconnect:
        manager.disconnect(room_id, websocket)
