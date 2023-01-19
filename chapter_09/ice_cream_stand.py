"""
Exercise 9-6

An ice cream stand is a specific kind of restaurant. Write a class
called IceCreamStand that inherits from the Restaurant class you wrote in
Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of the class
will work; just pick the one you like better. Add an attribute called flavors
that stores a list of ice cream flavors. Write a method that displays these
flavors. Create an instance of IceCreamStand, and call this method.
"""

from number_served import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='Ice Cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    def show_flavors(self):
        print('Flavor List:')
        for flavor in self.flavors:
            print(f'- {flavor}')


if __name__ == '__main__':
    stand = IceCreamStand(restaurant_name="Ben & Jerry's")
    stand.flavors = [
        'Chocolate',
        'Vanilla',
        'Strawberry',
        'Mint'
    ]
    stand.show_flavors()
