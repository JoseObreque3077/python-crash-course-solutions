"""
Exercise 11-1 and Exercise 11-2
TESTS FILE
"""
import unittest

from city_functions import get_formatted_location


class CitiesTestCase(unittest.TestCase):
    """Unit tests for 'city_functions.py' module."""
    
    def test_city_country(self):
        """Tests formatted location output with city and country data."""
        formatted_location = get_formatted_location(
            city='santiago',
            country='chile'
        )
        self.assertEqual(
            formatted_location,
            'Santiago, Chile'
        )
    
    def test_city_country_population(self):
        """
        Tests formatted location output with city, country and population data.
        """
        formatted_location = get_formatted_location(
            city='santiago',
            country='chile', 
            population=5_000_000
        )
        self.assertEqual(
            formatted_location,
            'Santiago, Chile - population 5000000'
        )


if __name__ == '__main__':
    unittest.main()
