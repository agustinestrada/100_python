import pandas as pd
import json

# Leer CSV
df = pd.read_csv("data.csv")

# Crear estructura anidada
data = {}
for _, row in df.iterrows():
    club = row["Club"]
    cancha = row["Cancha"]
    tee = row["Tee"]
    sexo = "Caballeros" if row["Sexo"] == "C" else "Damas"
    rating = row["Rating"]
    slope = row["Slope"]

    data.setdefault(club, {})
    data[club].setdefault(cancha, [])

    # Buscamos si ya existe ese Tee
    existing = next((t for t in data[club][cancha] if t["Tee"] == tee), None)
    if existing:
        existing[sexo] = {"Rating": rating, "Slope": slope}
    else:
        data[club][cancha].append({
            "Tee": tee,
            sexo: {"Rating": rating, "Slope": slope}
        })

# Guardar JSON bonito
with open("canchas.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)