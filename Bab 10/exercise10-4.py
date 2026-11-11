from pathlib import Path


guest_name = input("Siapa nama Anda? ")
guest_file = Path(__file__).with_name("guest.txt")
guest_file.write_text(f"{guest_name}\n", encoding="utf-8")
print(f"Nama {guest_name} sudah disimpan.")