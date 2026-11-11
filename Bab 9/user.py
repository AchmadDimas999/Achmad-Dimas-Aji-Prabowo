class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email

    def describe_user(self):
        print(f"Pengguna: {self.first_name} {self.last_name}")
        print(f"Usia: {self.age}")
        print(f"Lokasi: {self.location}")
        print(f"Surel: {self.email}")

    def greet_user(self):
        print(f"Halo, {self.first_name} {self.last_name}!")
