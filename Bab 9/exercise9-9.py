class Battery:
    def __init__(self, battery_size=50):
        self.battery_size = battery_size

    def get_range(self):
        return self.battery_size * 4

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")

    def get_range(self):
        print(
            f"Mobil ini dapat menempuh sekitar {self.battery.get_range()} mil "
            "dengan sekali pengisian daya."
        )


electric_car = ElectricCar("Nissan", "Leaf", 2024)
electric_car.get_range()

electric_car.battery.upgrade_battery()
electric_car.get_range()