import json
from pathlib import Path


user_info_file = Path(__file__).with_name("user_info.json")

user_info = {
    "nama": input("Siapa nama Anda? "),
    "usia": input("Berapa usia Anda? "),
    "kota": input("Di kota mana Anda tinggal? "),
}
user_info_file.write_text(json.dumps(user_info), encoding="utf-8")

remembered_info = json.loads(user_info_file.read_text(encoding="utf-8"))
print("\nBerikut informasi yang saya ingat tentang Anda:")
print(f"Nama: {remembered_info['nama']}")
print(f"Usia: {remembered_info['usia']}")
print(f"Kota: {remembered_info['kota']}")
