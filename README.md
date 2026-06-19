# Gebrauchtwagen-API (Portfolio Projekt)

Ein Full-Stack-Prototyp zur Abfrage von Gebrauchtwagen-Historien, inspiriert von Plattformen wie carVertical. Das Projekt demonstriert die nahtlose Verbindung zwischen einer Frontend-Benutzeroberfläche und einer validierenden Backend-API.

## Tech Stack

- **Backend:** Python, FastAPI, Uvicorn
- **Datenbank:** SQLite3
- **Frontend:** HTML5, CSS3, Vanilla JavaScript (Fetch API)

## Features

- **Strikte Input-Validierung:** Serverseitige Prüfung auf echte 17-stellige VIN-Standards (Ausschluss verbotener Zeichen wie I, O, Q).
- **RESTful API:** Saubere Endpunkte mit JSON-Responses und korrekten HTTP-Statuscodes (z.B. 404 für nicht gefundene Fahrzeuge, 400 für ungültige Eingaben).
- **Dynamische Daten:** Ein Python-Scraper/Generator füllt die SQLite-Datenbank mit realistischen Testdaten und passenden WMI-Codes (Herstellerkennungen).
- **CORS-Middleware:** Konfigurierte Sicherheitsrichtlinien für die Frontend-Backend-Kommunikation.

## Testdaten für die API

Da das System ungültige Eingaben blockiert, nutze bitte eine dieser generierten Test-VINs für die Suchmaske:

1. `WAUZZZ0MSNZ116800` Audi Q7
2. `WBAZZZKP3LD947328` BMW X5
3. `TMBZZZS05EC114165` Skoda Octavia RS

## Starten des Projekts

1. Virtuelle Umgebung aktivieren und Abhängigkeiten installieren.
2. Backend starten: `uvicorn api:app --reload`
3. Frontend (`index.html`) im Browser oder über einen Live Server öffnen.
