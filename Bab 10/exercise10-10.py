from pathlib import Path


chapter_directory = Path(__file__).parent
gutenberg_files = ("alice.txt", "pride_and_prejudice.txt")

for filename in gutenberg_files:
    file_path = chapter_directory / filename
    try:
        contents = file_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(
            f"File {filename} tidak ditemukan. Unduh teks dari Project Gutenberg "
            "dan simpan di folder Bab 10 dengan nama tersebut."
        )
        continue

    lowered_contents = contents.lower()
    print(f"\nAnalisis {filename}:")
    print(f"Kemunculan 'the': {lowered_contents.count('the')}")
    print(f"Kemunculan 'the ' (diikuti spasi): {lowered_contents.count('the ')}")