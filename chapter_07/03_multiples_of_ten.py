# Exercise 7-3
# Ask the user for a number, and then report whether the number
# is a multiple of 10 or not.

number = int(input("Please, input an integer number: "))

if number % 10 == 0 :
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} isn't a multiple of 10.")
