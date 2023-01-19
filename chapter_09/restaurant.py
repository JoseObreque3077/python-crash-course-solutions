"""
Exercise 9-1

Make a class called Restaurant.

The __init__() method for Restaurant should store two attributes:
a restaurant_name and a cuisine_type.

Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message
indicating that the restaurant is open.

Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.
"""


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print('Restautant Info:')
        print(f'Name: {self.restaurant_name}')
        print(f'Cuisine Type: {self.cuisine_type}\n')
    
    def open_restaurant(self):
        print('The restaurant is open!\n')


if __name__ == '__main__':
    restaurant = Restaurant(
        restaurant_name='The Gilded Truffle',
        cuisine_type='Gourmet'
    )
    
    # Instance attributes
    print(restaurant.restaurant_name)
    print(restaurant.cuisine_type)
    print()
    
    # Instance methods
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
