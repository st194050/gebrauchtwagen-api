import sqlite3
import random

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

status_unfallfrei = ["Ja", "Nein (Heckschaden)", "Nein (Vorderseite)", "Nein (Rückseite)", "Nein (Beide Seiten)"]

# random Autos generieren

for i in range(20):
    vin = f"WAUZZZ{random.randint(100000,999999)}"
    modell = random.choice(modelle)
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