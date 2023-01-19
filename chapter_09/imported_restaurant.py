"""
Exercise 9-10

Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant's methods to show that the import statement is
working properly.
"""

from number_served import Restaurant

restaurant = Restaurant(
    restaurant_name='Los Pollos Hermanos',
    cuisine_type='Fast Food'
)

restaurant.describe_restaurant()
