# Exercise 8-14
# Write a function that stores information about a car in a dictionary. The
# function should always receive a manufacturer and a model name. It should
# then accept an arbitrary number of keyword arguments. Call the function with
# the required information and two other name-value pairs, such as a color or
# an optional feature. Print the dictionary that’s returned to make sure all
# the information was stored correctly.

def make_car(manufacturer, model, **features):
    car = {
        'manufacturer': manufacturer,
        'model': model
    }
    return car | features  # Expression valid only in Python 3.9+

if __name__ == "__main__":
    car = make_car('subaru', 'outback', color='blue', tow_package=True)
    print(car)
