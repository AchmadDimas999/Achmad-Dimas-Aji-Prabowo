while True:
	usia = input("Berapa usia Anda? (ketik 'quit' untuk selesai): ")

	if usia == "quit":
		break

	usia = int(usia)
	if usia < 3:
		print("Tiket Anda gratis.")
	elif usia <= 12:
		print("Harga tiket Anda $10.")
	else:
		print("Harga tiket Anda $15.")
