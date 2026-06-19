from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sqlite3



app = FastAPI(title="Gebrauchtwagen-API", description="API für Gebrauchtwagen-Daten")

# Kommunikation zwischen Frontend und Backend erlauben
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Datenbankverbindung herstellen

def hole_auto_daten(vin: str):
    verbindung = sqlite3.connect('fahrzeuge.db')
    cursor = verbindung.cursor()

    cursor.execute('SELECT * FROM random_fahrzeuge WHERE vin = ?',(vin,))
    auto = cursor.fetchone()

    verbindung.close()
    return auto

# Routing
@app.get("/")
def startseite():
    return{"nachricht": "Willkommen bei der Gebrauchtwagen-API! Der Server läuft."}

@app.get("/api/report/{vin}")
def get_vehicle_report(vin: str):
    
    # Input validation
    if len(vin)!= 17:
        raise HTTPException(
            status_code=400,
            detail="Ungültige Eingabe: Die VIN muss genau 17 Stellen lang sein."
        )
    
    # Buchstaben I, O und Q nicht zulassen
    if any(verbotener_buchstabe in vin.upper() for verbotener_buchstabe in ["I", "O", "Q"]):
        raise HTTPException(
            status_code=400,
            detail="Ungültige VIN: Die Buchstaben I, O und Q sind nicht erlaubt"   
        )
    
    auto_daten = hole_auto_daten(vin)

    # Wenn fahrzeug nicht gefunden gebe 404 aus.
    if auto_daten is None:
        raise HTTPException(status_code=404, detail="Fahrzeug mit dieser VIN nicht gefunden")

   # wenn auto gefunden dann gebe auto_daten aus in JSON Format.
    return {
        "status": "erfolgreich",
        "daten": {
            "vin": auto_daten[0],
            "modell": auto_daten[1],
            "preis": auto_daten[2],
            "kilometerstand": auto_daten[3],
            "unfallfrei": auto_daten[4]
        }
    }
