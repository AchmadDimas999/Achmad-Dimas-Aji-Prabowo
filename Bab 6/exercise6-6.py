bahasa_favorit = {
    "Sarah": "Python",
    "Dimas": "JavaScript",
    "Jaden": "C",
    "Rina": "Python",
}

orang_yang_mengisi = ["Sarah", "Dimas", "Linus", "Rina", "Nadia"]

for nama in orang_yang_mengisi:
    if nama in bahasa_favorit:
        print(f"Terima kasih, {nama}, sudah mengisi jajak pendapat.")
    else:
        print(f"{nama}, silakan ikuti jajak pendapat bahasa pemrograman favorit.")