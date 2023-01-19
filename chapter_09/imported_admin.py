"""
Exercise 9-11

Start with your work from Exercise 9-8 (page 173). Store the
classes User, Privileges, and Admin in one module. Create a separate file,
make an Admin instance, and call show_privileges() to show that everything
is working correctly.
"""

from imported_admin_module import Admin

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
