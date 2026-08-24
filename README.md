# 🧭 Autonomy Map – Kollaboratives Tool für den Informatikunterricht

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=flat&logo=vuedotjs&logoColor=4FC08D)](https://vuejs.org/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Die **Autonomy Map** ist ein interaktives, webbasiertes Kollaborationstool zur didaktischen Strukturierung soziotechnischer Entscheidungen im Informatikunterricht (Lehrplanbereich *Informatik, Mensch und Gesellschaft*).

Das Tool ermöglicht es Schülerinnen und Schülern in Kleingruppen, komplexe Gestaltungs- und Nutzungsoptionen mit relevanten Akteuren in einer Matrix gegenüberzustellen, multiperspektivisch zu bewerten und ein fundiertes soziotechnisches Urteil zu fällen – **synchron, in Echtzeit und ohne Benutzerkonten**.

---

## ✨ Features

* 👥 **Multiplayer in Echtzeit:** Synchrone Kollaboration via WebSockets über einfache Raum-Codes (z. B. `MAP-123`).
* 📊 **Multiperspektivische Matrix:**
  * **Optionen (Zeilen):** Detaillierte Beschreibungen der technischen und organisatorischen Umsetzung per Klick hinterlegbar.
  * **Akteure (Spalten):** Erfassung von *Perspektive*, *Handlungsspielraum* und spezifischen *Werten* (Tag-System).
  * **Vollständigkeitsindikator:** Automatische visuelle Statusprüfung (`ℹ️ Info vollständig` / `⚠️ Info unvollständig`) an den Akteursköpfen.
* ⚖️ **Kriterienorientierte Bewertung:**
  * Stichpunktbasierte Argumentation in jeder Zelle mit Schnell-Klassifikation:
    * `+` **Vorteil / Chance** *(Grün)*
    * `-` **Nachteil / Risiko** *(Gelb)*
    * `!` **Ausschlusskriterium / Veto** *(Rot)*
  * Symbole lassen sich intuitiv per Klick umschalten.
* 📝 **Integrierte Urteilsbildung:** Zentrales Freitextfeld unter der Matrix zur Formulierung der abschließenden Güter- und Werteabwägung.
* ⚡ **Leichtgewichtig:** Keine Registrierungen, kein Node.js/npm-Build-Schritt, minimale Ladezeiten.

---

## 🛠️ Technologie-Stack

| Komponente | Technologie | Einsatzzweck |
| :--- | :--- | :--- |
| **Backend** | [FastAPI](https://fastapi.tiangolo.com/) (Python) | REST-API & asynchrones WebSocket-Raummanagement |
| **Server** | [Uvicorn](https://www.uvicorn.org/) | Performanter ASGI-Webserver |
| **Frontend** | [Vue.js 3](https://vuejs.org/) (CDN) | Reaktives State-Management im Browser |
| **Styling** | [Tailwind CSS](https://tailwindcss.com/) (CDN) | Modernes, responsives UI-Design |

---

## 🚀 Lokale Installation & Start

### Voraussetzungen
* Python 3.9+ installiert ([python.org](https://www.python.org/))
* Git installiert ([git-scm.com](https://git-scm.com/))

### 1. Repository klonen & Verzeichnis betreten
```bash
git clone https://github.com/NilsDyck/autonomy-map.git
cd autonomy-map
```

### 2. Virtuelle Umgebung erstellen (empfohlen)
```bash
# macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# Windows:
python -m venv venv
venv\Scripts\activate
```

### 3. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

### 4. Server starten
```bash
uvicorn main:app --reload
```
Die Anwendung ist nun lokal im Browser unter **`http://localhost:8000`** erreichbar.

---

## 🔒 Datenschutz & Sicherheit (Hosting via Render.com)

Beim Betrieb dieser Web-Applikation über den Cloud-Hosting-Dienst [Render.com](https://render.com) gelten folgende Prinzipien:

* **Datensparsamkeit:** Für die Nutzung ist keinerlei Registrierung nötig. Es werden keine Klarnamen, Passwörter oder Tracking-Cookies verarbeitet.
* **Pseudonyme Räume:** Der Zugriff und die Kollaboration erfolgen isoliert über zufällig generierte Raum-Codes.
* **Flüchtige Speicherung (In-Memory):** Eingegebene Inhalte werden nur temporär im Arbeitsspeicher des Servers gehalten und nicht dauerhaft in einer Datenbank archiviert. Nach Beendigung oder Leerlauf der Instanz werden alle Daten verworfen.
* **Verschlüsselung:** Alle Verbindungen (HTTP & WebSockets) sind standardmäßig per SSL/TLS (HTTPS/WSS) verschlüsselt.
* **Unterrichtshinweis:** Die Plattform ist ausschließlich für didaktische Inhalte gedacht. Nutzer:innen sind angehalten, **keine personenbezogenen Daten** in die Freitextfelder einzugeben.

> ℹ️ **Serverstandort:** Render.com betreibt Server u. a. in der EU-Region (*Frankfurt*). Für 100 % lokale Datenhoheit kann das Tool ohne Mehraufwand lokal im Klassen-/Schulnetz betrieben werden.

---

## 📄 Impressum & Kontakt

Dieses Projekt wurde für den Einsatz in Schule und Hochschule entwickelt.

**Angaben gemäß § 5 TMG / Verantwortlich für den Inhalt:**  
Nils Dyck  
Friedrich-Schiller-Universität Jena - Fakultät für Mathematik und Informatik - Abteilung Didaktik  
Inselplatz 5
07743 Jena  

**Kontaktmöglichkeiten:**  
* 📧 **E-Mail:** [nils.dyck@uni-jena.de]    
* 🐙 **GitHub:** [https://github.com/NilsDyck](https://github.com/NilsDyck)
