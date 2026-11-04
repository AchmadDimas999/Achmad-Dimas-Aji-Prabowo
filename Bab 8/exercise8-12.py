def make_sandwich(*items):
	"""Tampilkan bahan-bahan dalam pesanan sandwich."""
	print("Pesanan sandwich berisi:")
	for item in items:
		print(f"- {item}")


make_sandwich("keju", "tomat")
make_sandwich("ayam", "selada", "mayones")
make_sandwich("telur")
