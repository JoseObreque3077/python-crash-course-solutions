"""
Exercise 10-11

Write a program that prompts for the user’s favorite number.
Use json.dump() to store this number in a file. Write a separate program
that reads in this value and prints the message, “I know your favorite number!
It’s _____.”
"""
# Part 2: Retrieving the number from a JSON file

import json

filename = 'favorite_number.json'

try:
    with open(filename) as file:
        favorite_number = json.load(file)
except FileNotFoundError:
    pass
else:
    print(f"I know your favorite number! It's {favorite_number}.")
