from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


six_sided_die = Die()
print("Dadu 6 sisi:")
for _ in range(10):
    six_sided_die.roll_die()

ten_sided_die = Die(10)
print("\nDadu 10 sisi:")
for _ in range(10):
    ten_sided_die.roll_die()

twenty_sided_die = Die(20)
print("\nDadu 20 sisi:")
for _ in range(10):
    twenty_sided_die.roll_die()