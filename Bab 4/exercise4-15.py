def tampilkan_pizza():
    """Tampilkan pizza favorit."""
    jenis_pizza = ["margherita", "pepperoni", "jamur"]

    for pizza in jenis_pizza:
        print(f"Saya suka pizza {pizza}.")

    print("Saya benar-benar menyukai pizza!")


def tampilkan_potongan_kubus():
    """Tampilkan tiga bagian dari daftar kubus."""
    kubus = [angka ** 3 for angka in range(1, 11)]

    print("Tiga item pertama dalam daftar adalah:")
    print(kubus[:3])

    print("Tiga item dari tengah daftar adalah:")
    print(kubus[3:6])

    print("Tiga item terakhir dalam daftar adalah:")
    print(kubus[-3:])


def tampilkan_menu():
    """Tampilkan menu restoran yang diperbarui."""
    menu = ("nasi goreng", "sate", "soto", "gado-gado", "bakso")

    print("Menu awal restoran:")
    for makanan in menu:
        print(makanan)

    menu = ("mie goreng", "sate", "soto", "pecel", "bakso")

    print("Menu restoran yang baru:")
    for makanan in menu:
        print(makanan)


if __name__ == "__main__":
    tampilkan_pizza()
    tampilkan_potongan_kubus()
    tampilkan_menu()