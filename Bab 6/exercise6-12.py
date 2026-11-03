polling_bahasa = {
    "Sarah": {
        "bahasa": ["Python", "JavaScript"],
        "tahun_belajar": 2,
    },
    "Dimas": {
        "bahasa": ["JavaScript"],
        "tahun_belajar": 3,
    },
    "Jaden": {
        "bahasa": ["C", "Python"],
        "tahun_belajar": 1,
    },
}

print("HASIL JAJAK PENDAPAT BAHASA PEMROGRAMAN")
print("=" * 42)

for nama, informasi in polling_bahasa.items():
    bahasa = ", ".join(informasi["bahasa"])
    tahun = informasi["tahun_belajar"]
    print(f"{nama}:")
    print(f"  Bahasa favorit: {bahasa}")
    print(f"  Lama belajar: {tahun} tahun\n")