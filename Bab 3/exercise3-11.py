mountains = ["Mount Fuji", "Denali", "Kilimanjaro"]

try:
    print(mountains[3])
except IndexError:
    print("IndexError: index 3 berada di luar rentang list.")

print(f"Koreksi: {mountains[2]}")