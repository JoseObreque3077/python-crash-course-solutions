# Exercise 6-11
# Make a dictionary called cities. Use the names of three cities as keys in
# your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one
# fact about that city. The keys for each city’s dictionary should be something
# like country, population, and fact. Print the name of each city and all of
# the information you have stored about it.

cities = {
    "new york": {
        "country": "United States",
        "population": 8_467_513,
        "settled": 1624
    },
    "santiago": {
        "country": "Chile",
        "population": 6_903_479,
        "settled": 1540
    },
    "copenhague": {
        "country": "Denmark",
        "population": 2_135_634,
        "settled": 1160
    }
}

for city, city_info in cities.items():
    print(f"\nInfo about {city.title():}")
    for field, value in city_info.items():
        print(f"{field.title()}: {value}")
