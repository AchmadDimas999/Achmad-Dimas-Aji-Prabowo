def make_album(artist, title, number_of_songs=None):
	album = {"artist": artist, "title": title}
	if number_of_songs is not None:
		album["number_of_songs"] = number_of_songs
	return album


while True:
	artist = input("Masukkan nama artis (atau 'quit' untuk selesai): ")
	if artist.lower() == "quit":
		break

	title = input("Masukkan judul album: ")
	print(make_album(artist, title))
