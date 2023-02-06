"""
Exercise 10-7

Wrap your code from Exercise 10-6 in a while loop so the
user can continue entering numbers even if they make a mistake and enter text
instead of a number.
"""

print('Type "quit" to exit')
while True:
    try:
        input_1 = input('Enter the first number: ')
        if input_1 == 'quit':
            break
        
        input_2 = int(input('Enter the second number: '))
        if input_2 == 'quit':
            break
        
        input_1 = int(input_1)
        input_2 = int(input_2)
    except ValueError:
        print('The input must be a number!\n')
    else:
        print(f'{input_1} + {input_2} = {input_1 + input_2}\n')
