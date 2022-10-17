# Exercise 6-10
# Modify your program from Exercise 6-2 (page 99) so each
# person can have more than one favorite number. Then print each person’s name
# along with their favorite numbers.

favorite_numbers = {
    "Anthony": [7, 14],
    "Scott": [11, 13, 21],
    "Steve": [4, 19, 43, 68],
    "Natasha": [13],
    "Jennifer": [32, 99]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(number)
