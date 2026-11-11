from pathlib import Path


guest_names = []

while True:
    guest_name = input("Masukkan nama (kosong untuk selesai): ").strip()
    if not guest_name:
        break
    guest_names.append(guest_name)

guest_book_file = Path(__file__).with_name("guest_book.txt")
guest_book_file.write_text(
    "".join(f"{name}\n" for name in guest_names),
    encoding="utf-8",
)
print(f"{len(guest_names)} nama disimpan di buku tamu.")