"""
Exercise 9-5

Add an attribute called login_attempts to your User class from
Exercise 9-3 (page 162). Write a method called increment_login_attempts() that
increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.

Make an instance of the User class and call increment_login_attempts() several
times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""


class User():
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0
        
    def describe_user(self):
        print('User info:')
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'Age: {self.age}')
        print(f'Country: {self.country}\n')
        
    def greet_user(self):
        print(f'Hi {self.first_name} {self.last_name}!\n')
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


if __name__ == '__main__':
    user = User(
        first_name='Anthony',
        last_name='Stark',
        age=50,
        country='USA'
    )
    
    # Three login attempts are made
    user.increment_login_attempts()
    user.increment_login_attempts()
    user.increment_login_attempts()
    
    # Prints the login_attempts attribute value
    print(f'Login Attempts: {user.login_attempts}')
    
    # Resets the login_attempts attribute value
    user.reset_login_attempts()
    
    # Prints the login_attempts attribute value
    print(f'Login Attempts: {user.login_attempts}')
