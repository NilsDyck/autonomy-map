# 🧭 Autonomy Map – Kollaboratives Tool für den Informatikunterricht

Die **Autonomy Map** ist ein interaktives, kollaboratives Webtool zur didaktischen Strukturierung und ethischen Bewertung soziotechnischer Entscheidungen im Informatikunterricht (Themenbereich *Informatik, Mensch und Gesellschaft* / Informatikethik).

Das Tool ermöglicht es Schüler:innen in Gruppenarbeiten, Handlungsoptionen und Akteure in einer Matrix gegenüberzustellen, Kriterien multiperspektivisch zu bewerten und ein begründetes Urteil zu fällen – synchron und in Echtzeit per Raum-Code.

---

## ✨ Features

* **Multiplayer in Echtzeit:** Kollaboratives Arbeiten über WebSockets via Raum-Code (z. B. `MAP-123`) ohne Registrierungszwang.
* **Multiperspektivische Matrix:**
  * **Optionen (Zeilen):** Detaillierte Beschreibungen der technischen/organisatorischen Umsetzung per Klick hinterlegbar.
  * **Akteure (Spalten):** Erfassung von *Perspektive*, *Handlungsspielraum* und spezifischen *Werten* (Tags).
  * **Vollständigkeitsindikator:** Automatische Statusanzeige (`ℹ️ Info vollständig` / `⚠️ Info unvollständig`) an den Akteursköpfen.
* **Strukturierte Bewertung in den Zellen:**
  * Stichpunktbasierte Argumentation mit Symbol-Klassifikation:
    * `+` **Vorteil / Chance** (Grün)
    * `-` **Nachteil / Risiko** (Gelb)
    * `!` **Ausschlusskriterium / Veto** (Rot)
  * Symbole können durch Anklicken zyklisch gewechselt werden.
* **Urteilsbildung:** Großes Freitextfeld unter der Matrix zur Formulierung der abschließenden Güterabwägung.
* **Einfache Verwaltung:** Dynamisches Hinzufügen und Löschen von Optionen, Akteuren, Werten und Stichpunkten.

---

## 🛠️ Technologie-Stack

* **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python) mit asynchronen WebSockets für das Raum- und State-Management.
* **Server:** [Uvicorn](https://www.uvicorn.org/) als ASGI-Webserver.
* **Frontend:** [Vue.js 3](https://vuejs.org/) (Standalone CDN) & [Tailwind CSS](https://tailwindcss.com/) (kein Node.js/npm-Build-Schritt erforderlich).

---

## 🚀 Lokale Installation & Start

### Voraussetzungen
* Python 3.9 oder neuer
* Git

### 1. Repository klonen
```bash
git clone https://github.com/DEIN-NUTZERNAME/autonomy-map.git
cd autonomy-map
