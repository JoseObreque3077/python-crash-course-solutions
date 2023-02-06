"""
Exercise 10-3

Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
"""

filename = 'guest.txt'

name = input('Enter your name: ')

with open(filename, 'w') as file:
    file.write(name)
