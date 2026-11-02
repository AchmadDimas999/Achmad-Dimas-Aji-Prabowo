mobil = "subaru"
buah = ["apel", "jeruk", "mangga"]
angka = 10

print("Apakah mobil == 'subaru'? Saya prediksi True.")
print(mobil == "subaru")

print("\nApakah mobil == 'audi'? Saya prediksi False.")
print(mobil == "audi")

print("\nApakah mobil != 'audi'? Saya prediksi True.")
print(mobil != "audi")

print("\nApakah mobil != 'subaru'? Saya prediksi False.")
print(mobil != "subaru")

print("\nApakah mobil.lower() == 'subaru'? Saya prediksi True.")
print(mobil.upper().lower() == "subaru")

print("\nApakah mobil.lower() == 'audi'? Saya prediksi False.")
print(mobil.lower() == "audi")

print("\nApakah angka == 10? Saya prediksi True.")
print(angka == 10)

print("\nApakah angka == 5? Saya prediksi False.")
print(angka == 5)

print("\nApakah angka != 5? Saya prediksi True.")
print(angka != 5)

print("\nApakah angka != 10? Saya prediksi False.")
print(angka != 10)

print("\nApakah angka > 5? Saya prediksi True.")
print(angka > 5)

print("\nApakah angka > 10? Saya prediksi False.")
print(angka > 10)

print("\nApakah angka < 20? Saya prediksi True.")
print(angka < 20)

print("\nApakah angka < 10? Saya prediksi False.")
print(angka < 10)

print("\nApakah angka >= 10? Saya prediksi True.")
print(angka >= 10)

print("\nApakah angka >= 20? Saya prediksi False.")
print(angka >= 20)

print("\nApakah angka <= 10? Saya prediksi True.")
print(angka <= 10)

print("\nApakah angka <= 5? Saya prediksi False.")
print(angka <= 5)

print("\nApakah angka > 5 and angka < 15? Saya prediksi True.")
print(angka > 5 and angka < 15)

print("\nApakah angka > 5 and angka < 10? Saya prediksi False.")
print(angka > 5 and angka < 10)

print("\nApakah angka < 5 or angka == 10? Saya prediksi True.")
print(angka < 5 or angka == 10)

print("\nApakah angka < 5 or angka > 15? Saya prediksi False.")
print(angka < 5 or angka > 15)

print("\nApakah 'jeruk' ada di daftar buah? Saya prediksi True.")
print("jeruk" in buah)

print("\nApakah 'pisang' ada di daftar buah? Saya prediksi False.")
print("pisang" in buah)

print("\nApakah 'pisang' tidak ada di daftar buah? Saya prediksi True.")
print("pisang" not in buah)

print("\nApakah 'apel' tidak ada di daftar buah? Saya prediksi False.")
print("apel" not in buah)