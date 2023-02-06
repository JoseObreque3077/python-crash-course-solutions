"""
Exercise 10-4

Write a while loop that prompts users for their name. When they enter their
name, print a greeting to the screen and add a line recording their visit in a
file called guest_book.txt. Make sure each entry appears on a new line in
the file.
"""

filename = 'guest_book.txt'

print('Type "quit" to exit.\n')

while True:
    name = input('Enter your name: ')
    
    if name.lower() == 'quit':
        break
    
    with open(filename, 'a') as file:
        file.write(f'{name.title()}\n')
    
    print(f'Greetings, {name.title()}!\n')
