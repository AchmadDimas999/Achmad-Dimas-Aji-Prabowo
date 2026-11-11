from pathlib import Path


learning_file = Path(__file__).with_name("learning_python.txt")

print("Membaca seluruh isi file:")
contents = learning_file.read_text(encoding="utf-8")
print(contents)

print("Membaca file baris demi baris:")
lines = contents.splitlines()
for line in lines:
    print(line)