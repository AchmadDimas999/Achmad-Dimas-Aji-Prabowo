responses = {}

polling_active = True
while polling_active:
	name = input("Siapa nama Anda? ")
	place = input("Jika bisa mengunjungi satu tempat di dunia, ke mana Anda akan pergi? ")
	responses[name] = place

	repeat = input("Apakah orang lain ingin menjawab? (ya/tidak) ")
	if repeat.lower() != "ya":
		polling_active = False

print("\nHasil polling:")
for name, place in responses.items():
	print(f"{name} ingin mengunjungi {place}.")
