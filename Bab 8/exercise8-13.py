def build_profile(first, last, **user_info):
	"""Bangun dan kembalikan profil pengguna."""
	profile = {"first_name": first, "last_name": last}
	profile.update(user_info)
	return profile


user_profile = build_profile(
	"Budi",
	"Santoso",
	usia=20,
	kota="Jakarta",
	hobi="pemrograman",
)
print(user_profile)
