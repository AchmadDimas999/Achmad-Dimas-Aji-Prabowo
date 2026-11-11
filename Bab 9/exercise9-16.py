"""Catatan PyMOTW: modul random.

Saya membaca artikel random di https://pymotw.com/3/random/.
Modul random memakai generator pseudorandom Mersenne Twister. Fungsi
randint() berguna untuk memilih bilangan bulat dalam rentang tertentu,
sedangkan seed() dapat digunakan agar urutan hasil bisa diulang.
"""

import random


random.seed(10)
print(f"Contoh angka pseudorandom yang dapat diulang: {random.random():.3f}")