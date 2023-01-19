"""
Exercise 9-12

Store the User class in one module, and store the Privileges and Admin classes
in a separate module. In a separate file, create an Admin instance and call
show_privileges() to show that everything is still working correctly
"""

from multiple_modules_2 import Admin

admin = Admin(
    first_name='Jane',
    last_name='Doe',
    age=23,
    country='Spain'
)

admin.privileges.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]

admin.privileges.show_privileges()
