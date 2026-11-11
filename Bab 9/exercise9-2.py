class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} menyajikan masakan {self.cuisine_type}.")


restaurant_one = Restaurant("Sate Pak Budi", "Indonesia")
restaurant_two = Restaurant("Kedai Pasta", "Italia")
restaurant_three = Restaurant("Pojok Sushi", "Jepang")

restaurant_one.describe_restaurant()
restaurant_two.describe_restaurant()
restaurant_three.describe_restaurant()