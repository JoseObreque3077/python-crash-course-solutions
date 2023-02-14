"""
Exercise 11-1

Write a function that accepts two parameters: a city name and a
country name. The function should return a single string of the form
City, Country, such as Santiago, Chile. Store the function in a module called city_functions.py.
Create a file called test_cities.py that tests the function you just wrote
(remember that you need to import unittest and the function you want to test).
Write a method called test_city_country() to verify that calling your function
with values such as 'santiago' and 'chile' results in the correct string. Run test_cities.py, and make sure test_city_country() passes.

Exercise 11-2

Modify your function so it requires a third parameter, population. It
should now return a single string of the form City, Country - population xxx,
such as Santiago, Chile - population 5000000.

Run test_cities.py again. Make sure test_city_country() fails this time.

Modify the function so the population parameter is optional.

Run test_cities.py again, and make sure test_city_country() passes again.

Write a second test called test_city_country_population() that verifies
you can call your function with the values 'santiago', 'chile', and 'population=5000000'.

Run test_cities.py again, and make sure this new test passes.
"""

def get_formatted_location(city, country, population=None):
    """
    Generate a formatted location string with city, country and population data.
    """
    formatted_location = f'{city}, {country}'.title()
    
    if population:
        formatted_location += f' - population {population}'
    
    return formatted_location
