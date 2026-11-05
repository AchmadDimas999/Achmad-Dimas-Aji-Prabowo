sandwich_orders = ["tuna", "pastrami", "ayam", "keju"]
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f"Saya membuat sandwich {sandwich} untuk Anda.")
	finished_sandwiches.append(sandwich)

print("Sandwich yang sudah dibuat:")
for sandwich in finished_sandwiches:
	print(sandwich)
