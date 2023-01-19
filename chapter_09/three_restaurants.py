"""
Exercise 9-2

Start with your class from Exercise 9-1. Create three different
instances from the class, and call describe_restaurant() for each instance.
"""

from restaurant import Restaurant

restaurant_1 = Restaurant(
    restaurant_name='Los Pollos Hermanos',
    cuisine_type='Fast Food'
)

restaurant_2 = Restaurant(
    restaurant_name='The Guilded Truffle',
    cuisine_type='Gourmet'
)

restaurant_3 = Restaurant(
    restaurant_name="Panucci's Pizza",
    cuisine_type='Fast Food'
)

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
