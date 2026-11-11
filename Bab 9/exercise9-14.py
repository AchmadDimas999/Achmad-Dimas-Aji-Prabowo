from random import sample


lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E"]
winning_ticket = sample(lottery_items, k=4)

print(f"Tiket yang menang: {winning_ticket}")
print("Tiket yang cocok dengan keempat angka atau huruf ini memenangkan hadiah!")