import sqlite3
import random

def generiere_echte_vin(modell_name):
    #  Marke feststellen (erstes Wort des Modells)
    marke = modell_name.split()[0]
    
    #  Passender WMI aus dem Dictionairy wählen
    wmi = wmi_katalog.get(marke, "ZZZ")
    
    # 3. Modell/Füllzeichen (6 Stellen)
    erlaubte_zeichen = "ABCDEFGHJKLMNPRSTVWXYZ0123456789"
    vds = "ZZZ" + "".join(random.choices(erlaubte_zeichen, k=3))
    
    # 4. Baujahr und Werk (2 Stellen)
    jahr = random.choice("ABCDEFGHJKLMNPRSTVWXY")
    werk = random.choice(erlaubte_zeichen)
    
    # 5. Seriennummer (6 Stellen)
    serie = str(random.randint(100000, 999999))
    
    return wmi + vds + jahr + werk + serie

verbindung = sqlite3.connect('fahrzeuge.db')
cursor = verbindung.cursor()

cursor.execute('''
   CREATE TABLE IF NOT EXISTS random_fahrzeuge (
    vin TEXT PRIMARY KEY,
    modell TEXT,
    preis INTEGER,
    kilometerstand INTEGER,
    unfallfrei TEXT
    )
''')

# Bausteine für die zufällige Auswahl

modelle = [
    "VW Golf VIII 2.0 TDI", "BMW 320i xDrive", "Audi A4 Avant", 
    "Mercedes C 220 d", "Tesla Model 3", "Ford Focus 1.5 EcoBoost",
    "Skoda Octavia RS", "Toyota Corolla Hybrid", "Peugeot 308 GT Line",
    "Hyundai Tucson 2.0", "Nissan Qashqai", "Opel Astra",
    "Renault Megane", "Volvo XC60", "Jeep Cherokee",
    "Land Rover Discovery", "Fiat 500", "Citroën C5 Aircross",
    "Suzuki Swift", "Kia Sportage", "Mazda CX-5",
    "Honda CR-V", "Volkswagen Passat", "Audi A3 Sportback",
    "Mercedes E-Klasse", "BMW 520d", "Audi A4 Limousine",
    "Mercedes S-Klasse", "BMW 740d", "Audi A8 L",
    "Mercedes G-Klasse", "BMW X5", "Audi Q7",
    "Mercedes GLC", "BMW X3", "Audi Q5",
]

# WMI Dictionairy
wmi_katalog = {
    "VW": "WVW", "Volkswagen": "WVW",
    "Audi": "WAU",
    "BMW": "WBA",
    "Mercedes": "WDD",
    "Tesla": "5YJ",
    "Ford": "WF0",
    "Skoda": "TMB",
    "Toyota": "JT1",
    "Peugeot": "VF3",
    "Hyundai": "KMH",
    "Nissan": "JN1",
    "Opel": "W0L",
    "Renault": "VF1",
    "Volvo": "YV1",
    "Jeep": "1C4",
    "Land": "SAL",    # Für Land Rover
    "Fiat": "ZFA",
    "Citroën": "VF7",
    "Suzuki": "JSA",
    "Kia": "KNA",
    "Mazda": "JMZ",
    "Honda": "JHM"
}

status_unfallfrei = ["Ja", "Nein (Heckschaden)", "Nein (Vorderseite)", "Nein (Rückseite)", "Nein (Beide Seiten)"]

# random Autos generieren

for i in range(20):
    # Auto bestimmen
    modell = random.choice(modelle)
    
    # VIN passend zum Auto generieren lassen
    vin = generiere_echte_vin(modell)
    preis = random.randint(10000, 80000)
    kilometerstand = random.randint(100, 250000)
    unfall = random.choice(status_unfallfrei)
    
    cursor.execute('''
      INSERT OR REPLACE INTO random_fahrzeuge(vin, modell, preis, kilometerstand, unfallfrei)
      VALUES (?, ?, ?, ?, ?)
    ''', (vin, modell, preis, kilometerstand, unfall))

verbindung.commit()

cursor.execute('SELECT * FROM random_fahrzeuge LIMIT 5')
erste_5 = cursor.fetchall()

print("Die ersten 5 zufälligen Fahrzeuge:")
for fahrzeug in erste_5:
    print(f"Fahrzeug: {fahrzeug[1]} (VIN: {fahrzeug[0]}), Preis: {fahrzeug[2]}€, Kilometerstand: {fahrzeug[3]}km, Unfallfrei: {fahrzeug[4]}")