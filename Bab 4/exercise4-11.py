jenis_pizza = ["margherita", "pepperoni", "jamur"]
friend_pizzas = jenis_pizza[:]

jenis_pizza.append("keju")
friend_pizzas.append("nanas")

print("Pizza favorit saya:")
for pizza in jenis_pizza:
    print(pizza)

print("Pizza favorit teman saya:")
for pizza in friend_pizzas:
    print(pizza)