"""
Exercise 9-3

Make a class called User.

Create two attributes called first_name and last_name, and then create several
other attributes that are typically stored in a user profile.

Make a method called describe_user() that prints a summary of the user's
information.

Make another method called greet_user() that prints a personalized
greeting to the user.

Create several instances representing different users, and call both methods
for each user.
"""


class User():
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        
    def describe_user(self):
        print('User info:')
        print(f'First Name: {self.first_name}')
        print(f'Last Name: {self.last_name}')
        print(f'Age: {self.age}')
        print(f'Country: {self.country}\n')
        
    def greet_user(self):
        print(f'Hi {self.first_name} {self.last_name}!\n')
        

if __name__ == '__main__':
    user_1 = User(
        first_name='Homer',
        last_name='Simpson',
        age=47,
        country='United States of America'
    )
    
    user_2 = User(
        first_name='Charles',
        last_name='Burns',
        age=999,
        country='United States of America'
    )
    
    user_3 = User(
        first_name='nospmiS',
        last_name='remoH',
        age=74,
        country='Greece'
    )
    
    user_1.describe_user()
    user_1.greet_user()
    
    user_2.describe_user()
    user_2.greet_user()
    
    user_3.describe_user()
    user_3.greet_user()
