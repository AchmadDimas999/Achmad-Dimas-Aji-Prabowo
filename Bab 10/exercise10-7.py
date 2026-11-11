print("Kalkulator penjumlahan (tekan Enter tanpa angka untuk keluar)")

while True:
    first_input = input("Masukkan angka pertama: ").strip()
    if not first_input:
        break

    second_input = input("Masukkan angka kedua: ").strip()
    if not second_input:
        break

    try:
        first_number = int(first_input)
        second_number = int(second_input)
    except ValueError:
        print("Input tidak valid. Masukkan angka bulat dan coba lagi.")
    else:
        print(f"Hasil penjumlahan: {first_number + second_number}")

print("Kalkulator selesai.")