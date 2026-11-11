from pathlib import Path


learning_file = Path(__file__).with_name("learning_python.txt")
contents = learning_file.read_text(encoding="utf-8")

for line in contents.splitlines():
    print(line)