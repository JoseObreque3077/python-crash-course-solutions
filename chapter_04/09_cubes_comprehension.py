# Exercise 4-9:
# Use a list comprehension to generate a list of the first 10 cubes.

cubes = [x ** 3 for x in range(1, 11)]

for number in cubes:
    print(number)
