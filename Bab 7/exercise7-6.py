topping = input("Masukkan topping pizza (ketik 'quit' untuk selesai): ")
while topping != "quit":
	print(f"Saya akan menambahkan {topping} ke pizza Anda.")
	topping = input("Masukkan topping lain (ketik 'quit' untuk selesai): ")

loop_aktif = True
while loop_aktif:
	topping = input("Masukkan topping pizza (ketik 'quit' untuk selesai): ")
	if topping == "quit":
		loop_aktif = False
	else:
		print(f"Saya akan menambahkan {topping} ke pizza Anda.")

while True:
	topping = input("Masukkan topping pizza (ketik 'quit' untuk selesai): ")
	if topping == "quit":
		break
	print(f"Saya akan menambahkan {topping} ke pizza Anda.")
