# Exercise 8-6
# Write a function called city_country() that takes in the name of a
# city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the
# values that are returned.

def city_country(city, country):
    return f"{city.title()}, {country.title()}"


if __name__ == "__main__":
    print(city_country("Villarrica", "Chile"))
    print(city_country("Oslo", "Norway"))
    print(city_country("Berlin", "Germany"))
