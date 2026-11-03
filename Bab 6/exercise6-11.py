cities = {
    "Jakarta": {
        "negara": "Indonesia",
        "populasi": 10_600_000,
        "fakta": "Merupakan salah satu pusat ekonomi dan pemerintahan Indonesia.",
    },
    "Tokyo": {
        "negara": "Jepang",
        "populasi": 14_000_000,
        "fakta": "Memiliki jaringan kereta dan transportasi umum yang luas.",
    },
    "Kairo": {
        "negara": "Mesir",
        "populasi": 10_000_000,
        "fakta": "Terletak dekat dengan Piramida Giza.",
    },
}

for nama_kota, informasi in cities.items():
    print(f"\n{nama_kota}")
    print(f"  Negara: {informasi['negara']}")
    print(f"  Perkiraan populasi: {informasi['populasi']:,} jiwa")
    print(f"  Fakta: {informasi['fakta']}")