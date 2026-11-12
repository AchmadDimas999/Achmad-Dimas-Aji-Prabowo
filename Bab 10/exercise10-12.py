import json
from pathlib import Path


favorite_number_file = Path(__file__).with_name("favorite_number.json")

try:
    favorite_number = json.loads(favorite_number_file.read_text(encoding="utf-8"))
except FileNotFoundError:
    favorite_number = input("Berapa angka favorit Anda? ")
    favorite_number_file.write_text(json.dumps(favorite_number), encoding="utf-8")
    print("Angka favorit Anda sudah disimpan.")
else:
    print(f"Saya tahu angka favorit Anda! Angkanya {favorite_number}.")
