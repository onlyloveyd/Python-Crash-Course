class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f'FirstName = {self.first_name},LastName = {self.last_name}')

    def greet_user(self):
        print(f'Hello, {self.first_name}')


user_python = User('py', 'thon')
user_python.describe_user()
user_python.greet_user()

user_kotlin = User('kot', 'lin')
user_kotlin.describe_user()
user_kotlin.greet_user()

user_java = User('ja', 'va')
user_java.describe_user()
user_java.greet_user()
