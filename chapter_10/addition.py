"""
Exercise 10-7

One common problem when prompting for numerical input occurs
when people provide text instead of numbers. When you try to convert the input
to an int, you'll get a ValueError. Write a program that prompts for two
numbers. Add them together and print the result. Catch the ValueError if either
input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.
"""

try:
    input_1 = int(input('Enter the first number: '))
    input_2 = int(input('Enter the second number: '))
except ValueError:
    print('The input must be a number!')
else:
    print(f'{input_1} + {input_2} = {input_1 + input_2}')
