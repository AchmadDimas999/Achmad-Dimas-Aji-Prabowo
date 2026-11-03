sungai_dan_negara = {
    "Nil": "Mesir",
    "Amazon": "Brasil",
    "Gangga": "India",
}

for sungai, negara in sungai_dan_negara.items():
    print(f"Sungai {sungai} mengalir melalui {negara}.")

print("\nNama sungai:")
for sungai in sungai_dan_negara:
    print(sungai)

print("\nNama negara:")
for negara in sungai_dan_negara.values():
    print(negara)