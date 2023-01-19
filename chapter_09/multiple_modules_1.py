"""
Module used in exercise 9-12
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
