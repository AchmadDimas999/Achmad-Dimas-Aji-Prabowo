class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"Pengguna: {self.first_name} {self.last_name}")
        print(f"Usia: {self.age}")
        print(f"Lokasi: {self.location}")
        print(f"Surel: {self.email}")

    def greet_user(self):
        print(f"Halo, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User("Dimas", "Prabowo", 21, "Jakarta", "dimas@example.com")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Jumlah percobaan masuk: {user.login_attempts}")

user.reset_login_attempts()
print(f"Jumlah percobaan masuk setelah diatur ulang: {user.login_attempts}")