"""
Exercise 9-4

Start with your program from Exercise 9-1 (page 162). Add an attribute called
number_served with a default value of 0. Create an instance called
restaurant from this class. Print the number of customers the restaurant has
served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number of
customers that have been served. Call this method with a new number and print
the value again.

Add a method called increment_number_served() that lets you increment the
number of customers who've been served. Call this method with any number you
like that could represent how many customers were served in, say, a day of
business.
"""


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print('Restautant Info:')
        print(f'Name: {self.restaurant_name}')
        print(f'Cuisine Type: {self.cuisine_type}\n')
    
    def open_restaurant(self):
        print('The restaurant is open!\n')
        
    def set_number_served(self, value):
        self.number_served = value
    
    def increment_number_served(self, value):
        self.number_served += value


if __name__ == '__main__':
    restaurant = Restaurant(
        restaurant_name='Boragó',
        cuisine_type='Gourmet Chilean indigenous cuisine'
    )
    
    # Number of customers served
    print(f'Customers served: {restaurant.number_served}')
    restaurant.number_served = 100
    print(f'Customers served: {restaurant.number_served}')
    
    # Sets the 'number_served' attribute value via the
    # 'set_number_served' method.
    restaurant.set_number_served(200)
    print(f'Customers served: {restaurant.number_served}')

    # Adds an increment to the 'served_value' attribute using
    # the 'increment_served_value' method.
    restaurant.increment_number_served(75)
    print(f'Customers served: {restaurant.number_served}')
