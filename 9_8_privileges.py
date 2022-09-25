class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f'FirstName = {self.first_name},LastName = {self.last_name}')

    def greet_user(self):
        print(f'Hello, {self.first_name}')


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)


admin = Admin('Yi', 'Dong', ["can add post", "can delete post", "can ban user"])
admin.privileges.show_privileges()
