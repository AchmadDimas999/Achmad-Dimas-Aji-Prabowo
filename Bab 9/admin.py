from user import User


class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = [
                "dapat menambahkan unggahan",
                "dapat menghapus unggahan",
                "dapat memblokir pengguna",
            ]
        self.privileges = privileges

    def show_privileges(self):
        print("Hak istimewa administrator:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = Privileges()
