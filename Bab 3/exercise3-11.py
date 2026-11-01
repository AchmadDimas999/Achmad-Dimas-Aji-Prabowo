mountains = ["Mount Fuji", "Denali", "Kilimanjaro"]

try:
    print(mountains[3])
except IndexError:
    print("IndexError: index 3 is outside the list.")

print(f"Corrected index: {mountains[2]}")