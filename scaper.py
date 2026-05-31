import json
import random
import os

# Database di base con i modelli e le specifiche tecniche reali
base_moto = [
    {"brand": "Vespa", "model": "Primavera 50", "license": "AM", "style": "Scooter", "cc": 49, "power": 3, "base_price": 3990, "tags": ["citta", "economico", "scooter", "comodo", "casa lavoro"]},
    {"brand": "Beta", "model": "RR 50 Motard", "license": "AM", "style": "Motard", "cc": 49, "power": 4, "base_price": 3500, "tags": ["divertente", "marce", "motard", "agile", "ragazzi"]},
    {"brand": "KTM", "model": "Duke 125", "license": "A1", "style": "Naked", "cc": 125, "power": 11, "base_price": 5500, "tags": ["naked", "sportivo", "ragazzi", "agile", "scattante"]},
    {"brand": "Yamaha", "model": "YZF-R125", "license": "A1", "style": "Sportiva", "cc": 125, "power": 11, "base_price": 5800, "tags": ["pista", "carenata", "sportiva", "corsa", "velocita"]},
    {"brand": "Honda", "model": "SH125i", "license": "A1", "style": "Scooter", "cc": 125, "power": 9, "base_price": 3800, "tags": ["citta", "casa lavoro", "scooter", "ruote alte"]},
    {"brand": "Yamaha", "model": "MT-07 (Depotenziata)", "license": "A2", "style": "Naked", "cc": 689, "power": 35, "base_price": 7900, "tags": ["naked", "potente", "divertente", "coppia", "versatile"]},
    {"brand": "Honda", "model": "NX500", "license": "A2", "style": "Touring", "cc": 471, "power": 35, "base_price": 7300, "tags": ["viaggio", "avventura", "crossover", "comoda", "turismo"]},
    {"brand": "Kawasaki", "model": "Ninja 400", "license": "A2", "style": "Sportiva", "cc": 399, "power": 33, "base_price": 6500, "tags": ["sportiva", "carenata", "pista", "leggera"]},
    {"brand": "Benelli", "model": "TRK 502", "license": "A2", "style": "Touring", "cc": 500, "power": 35, "base_price": 5990, "tags": ["turismo", "imponente", "viaggio", "borse", "economico"]},
    {"brand": "Ducati", "model": "Monster", "license": "A", "style": "Naked", "cc": 937, "power": 82, "base_price": 12300, "tags": ["naked", "potente", "rossa", "sound", "sportiva"]},
    {"brand": "BMW", "model": "R 1300 GS", "license": "A", "style": "Touring", "cc": 1300, "power": 107, "base_price": 21000, "tags": ["viaggio", "premium", "boxer", "turismo", "comoda"]},
    {"brand": "Yamaha", "model": "YZF-R1", "license": "A", "style": "Sportiva", "cc": 998, "power": 147, "base_price": 20200, "tags": ["pista", "velocissima", "estrema", "4 cilindri"]},
    {"brand": "Harley-Davidson", "model": "Nightster", "license": "A", "style": "Custom", "cc": 975, "power": 66, "base_price": 15900, "tags": ["custom", "passeggiata", "sella bassa", "relax"]}
]

def update_prices():
    updated_list = []
    for moto in base_moto:
        # Il robot simula una variazione di prezzo di mercato o sconti della notte (+/- 2%)
        variation = random.randint(-150, 150)
        current_price = moto["base_price"] + variation
        
        updated_list.append({
            "brand": moto["brand"],
            "model": moto["model"],
            "license": moto["license"],
            "style": moto["style"],
            "cc": moto["cc"],
            "power": moto["power"],
            "price": current_price,
            "tags": moto["tags"]
        })
    
    # Salva il file JSON che verrà letto dal sito web
    with open("moto.json", "w", encoding="utf-8") as f:
        json.dump(updated_list, f, indent=4, ensure_ascii=False)
    print("Database JSON aggiornato con successo dal Robot!")

if __name__ == "__main__":
    update_prices()
