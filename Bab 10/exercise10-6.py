print("Kalkulator penjumlahan")

try:
    first_number = int(input("Masukkan angka pertama: "))
    second_number = int(input("Masukkan angka kedua: "))
except ValueError:
    print("Input tidak valid. Masukkan angka bulat, ya.")
else:
    print(f"Hasil penjumlahan: {first_number + second_number}")