from random import sample


lottery_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E"]
my_ticket = [7, 3, "A", "D"]

draw_count = 0
while True:
    drawn_ticket = sample(lottery_items, k=4)
    draw_count += 1
    if set(drawn_ticket) == set(my_ticket):
        break

print(f"Tiket saya: {my_ticket}")
print(f"Jumlah pengundian sampai menang: {draw_count}")