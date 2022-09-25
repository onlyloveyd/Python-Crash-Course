from privileges import Privileges
from user import User


class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(privileges)
