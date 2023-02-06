"""
Exercise 10-12

Combine the two programs from Exercise 10-
11 into one file. If the number is already stored, report the favorite number
to the user.
If not, prompt for the user’s favorite number and store it in a file.
Run the program twice to see that it works.
"""

import json

def dump_favorite_number(filename):
    """Prompts for a favorite number and store it in a JSON file."""
    try:
        favorite_number = int(input('What is your favorite number? '))
    except ValueError:
        print("This isn't a number!")
    else:
        with open(filename, 'w') as file:
            json.dump(favorite_number, file)
            print("I'll remember your choice!")

def retrieve_favorite_number(filename):
    """Retrieves a favorite number from a JSON file."""
    with open(filename) as file:
        favorite_number = json.load(file)
    
    return favorite_number
    
if __name__ == '__main__':
    filename = 'favorite_number_remembered.json'
    
    try:
        favorite_number = retrieve_favorite_number(filename)
    except FileNotFoundError:
        dump_favorite_number(filename)
    else:
        print(f"I know your favorite number! It's {favorite_number}.")
