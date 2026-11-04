"""Contoh lima cara mengimpor dan memanggil fungsi."""

import book_functions
from book_functions import favorite_book
from book_functions import favorite_book as print_favorite_book
import book_functions as bf
from book_functions import *

book_functions.favorite_book("Bumi Manusia")
favorite_book("Laut Bercerita")
print_favorite_book("Pulang")
bf.favorite_book("Cantik Itu Luka")
favorite_book("Laskar Pelangi")
