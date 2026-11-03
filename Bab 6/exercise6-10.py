angka_favorit = {
    "Dimas": [7, 17],
    "Sarah": [12, 24],
    "Jaden": [3],
    "Rina": [21, 42],
    "Linus": [42, 64],
}

for nama, angka in angka_favorit.items():
    daftar_angka = ", ".join(str(nilai) for nilai in angka)
    print(f"Angka favorit {nama}: {daftar_angka}.")