"""
Exercise 9-7

An administrator is a special kind of user. Write a class called Admin that
inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise
9-5 (page 167). Add an attribute, privileges, that stores a list of strings like
"can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator's set of
privileges. Create an instance of Admin, and call your method.
"""

from login_attempts import User


class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.privileges = []
        
    def show_privileges(self):
        print('Privileges:')
        for privilege in self.privileges:
            print(f'- {privilege}')


if __name__ == '__main__':
    admin = Admin(
        first_name='John',
        last_name='Doe',
        age=18,
        country='Iceland'
    )
    
    admin.privileges = [
        'can reset passwords',
        'can moderate discussions',
        'can suspend accounts',
    ]
    
    admin.show_privileges()
