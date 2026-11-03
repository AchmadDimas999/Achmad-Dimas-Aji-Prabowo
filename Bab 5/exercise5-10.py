current_users = ["Dimas", "Sarah", "Jaden", "admin", "Linus"]
new_users = ["sarah", "Michael", "Rina", "ADMIN", "Nadia"]

current_users_lowercase = [username.lower() for username in current_users]

for new_username in new_users:
    if new_username.lower() in current_users_lowercase:
        print(f"Nama pengguna '{new_username}' sudah digunakan. Silakan masukkan nama lain.")
    else:
        print(f"Nama pengguna '{new_username}' tersedia.")