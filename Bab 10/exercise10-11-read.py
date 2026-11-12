import json
from pathlib import Path


favorite_number_file = Path(__file__).with_name("favorite_number.json")
favorite_number = json.loads(favorite_number_file.read_text(encoding="utf-8"))
print(f"Saya tahu angka favorit Anda! Angkanya {favorite_number}.")
