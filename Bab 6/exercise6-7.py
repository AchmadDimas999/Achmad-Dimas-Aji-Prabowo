
orang_1 = {
    "first_name": "Dimas",
    "last_name": "Prabowo",
    "age": 20,
    "city": "Jakarta",
}

orang_2 = {
    "first_name": "Sarah",
    "last_name": "Wijaya",
    "age": 22,
    "city": "Bandung",
}

orang_3 = {
    "first_name": "Jaden",
    "last_name": "Pratama",
    "age": 19,
    "city": "Surabaya",
}

people = [orang_1, orang_2, orang_3]

for orang in people:
    print(
        f"{orang['first_name']} {orang['last_name']} berusia "
        f"{orang['age']} tahun dan tinggal di {orang['city']}."
    )
