from pathlib import Path


chapter_directory = Path(__file__).parent

for filename in ("cats.txt", "dogs.txt"):
    file_path = chapter_directory / filename
    try:
        contents = file_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        print(f"\nIsi file {filename}:")
        print(contents, end="" if contents.endswith("\n") else "\n")