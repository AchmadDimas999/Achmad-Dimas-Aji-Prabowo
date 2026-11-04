sandwich_orders = ["tuna", "pastrami", "ayam", "pastrami", "keju", "pastrami"]
finished_sandwiches = []

print("Toko kehabisan pastrami.")
while "pastrami" in sandwich_orders:
	sandwich_orders.remove("pastrami")

while sandwich_orders:
	sandwich = sandwich_orders.pop(0)
	print(f"Saya membuat sandwich {sandwich} untuk Anda.")
	finished_sandwiches.append(sandwich)

print("Sandwich yang sudah dibuat:")
for sandwich in finished_sandwiches:
	print(sandwich)
