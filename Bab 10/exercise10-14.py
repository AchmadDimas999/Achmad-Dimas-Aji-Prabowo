import json
from pathlib import Path


username_file = Path(__file__).with_name("username.json")


def get_new_username():
    """Minta username baru dan simpan ke file."""
    username = input("Siapa nama Anda? ")
    username_file.write_text(json.dumps(username), encoding="utf-8")
    return username


def greet_user():
    """Sapa pengguna setelah memastikan username yang tersimpan benar."""
    try:
        username = json.loads(username_file.read_text(encoding="utf-8"))
    except FileNotFoundError:
        username = get_new_username()
        print(f"Senang bertemu dengan Anda, {username}!")
    else:
        is_correct_username = input(
            f"Apakah username Anda {username}? (y/t): "
        ).strip().lower()
        if is_correct_username == "y":
            print(f"Selamat datang kembali, {username}!")
        else:
            username = get_new_username()
            print(f"Username baru Anda sudah disimpan. Senang bertemu, {username}!")


greet_user()
