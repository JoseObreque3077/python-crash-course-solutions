"""
Exercise 10-11

Write a program that prompts for the user’s favorite number.
Use json.dump() to store this number in a file. Write a separate program
that reads in this value and prints the message, “I know your favorite number!
It’s _____.”
"""
# Part 1: Storing the number on a JSON file

import json

filename = 'favorite_number.json'

try:
    favorite_number = int(input('What is your favorite number? '))
except ValueError:
    print("This isn't a number!")
else:
    with open(filename, 'w') as file:
        json.dump(favorite_number, file)
        print("I'll remember your choice!")
