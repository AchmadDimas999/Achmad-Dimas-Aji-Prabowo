class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} menyajikan masakan {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka.")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("Rasa es krim yang tersedia:")
        for flavor in self.flavors:
            print(f"- {flavor}")


ice_cream_stand = IceCreamStand(
    "Pojok Es Krim",
    "es krim",
    ["vanila", "cokelat", "stroberi"],
)
ice_cream_stand.display_flavors()