users = ["admin","rusdi","dimas"]

if users:
    for username in users:
        if username == "admin":
            print("Halo admin, apakah Anda ingin melihat laporan status?")
        else:
            print(f"Halo {username}, terima kasih telah masuk kembali.")
else:
    print("Kita perlu mencari beberapa pengguna!")