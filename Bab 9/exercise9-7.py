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


class Admin(User):
    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = [
            "dapat menambahkan unggahan",
            "dapat menghapus unggahan",
            "dapat memblokir pengguna",
        ]

    def show_privileges(self):
        print("Hak istimewa administrator:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Admin("Dimas", "Prabowo", 21, "Jakarta", "dimas@example.com")
admin.show_privileges()