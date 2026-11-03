hewan_peliharaan_1 = {
    "jenis": "kucing",
    "pemilik": "Sarah",
}

hewan_peliharaan_2 = {
    "jenis": "anjing",
    "pemilik": "Dimas",
}

hewan_peliharaan_3 = {
    "jenis": "kelinci",
    "pemilik": "Jaden",
}

pets = [hewan_peliharaan_1, hewan_peliharaan_2, hewan_peliharaan_3]

for hewan in pets:
    print(f"Jenis hewan: {hewan['jenis']}")
    print(f"Nama pemilik: {hewan['pemilik']}\n")