menu = ("nasi goreng", "sate", "soto", "gado-gado", "bakso")

print("Makanan yang tersedia di restoran:")
for makanan in menu:
    print(makanan)

try:
    menu[0] = "mie goreng"
except TypeError:
    print("Perubahan ditolak: item dalam tuple tidak dapat diubah.")

menu = ("mie goreng", "sate", "soto", "pecel", "bakso")

print("Menu restoran yang baru:")
for makanan in menu:
    print(makanan)