"""
Module used in exercise 9-12
"""
from multiple_modules_1 import User


class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges
    
    def show_privileges(self):
        print('Privileges:')
        for privilege in self.privileges:
            print(f'- {privilege}')


class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges()
