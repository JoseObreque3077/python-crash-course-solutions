"""
Exercise 9-8

Write a separate Privileges class. The class should have one attribute,
privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance as
an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
"""
from login_attempts import User


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


if __name__ == '__main__':
    admin = Admin(
        first_name='John',
        last_name='Doe',
        age=18,
        country='Iceland'
    )
    
    admin.privileges.privileges = [
        'can reset passwords',
        'can moderate discussions',
        'can suspend accounts',
    ]
    
    admin.privileges.show_privileges()
    