# Exercise 8-5
# Write a function called describe_city() that accepts the name of a city
# and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not
# in the default country

def describe_city(city, country="Chile"):
    print(f"{city.title()} is in {country.title()}.")


if __name__ == "__main__":
    describe_city(city="Concepción")
    describe_city("Reykjavik", "Iceland")
    describe_city("Paris", "France")
