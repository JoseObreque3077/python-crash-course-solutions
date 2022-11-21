# Exercise 6-7
# Start with the program you wrote for Exercise 6-1 (page 99). Make two
# new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As
# you loop through the list, print everything you know about each person

person_1 = {
    "first_name": "Anthony",
    "last_name": "Stark",
    "age": 42,
    "city": "Long Island, NY"
}

person_2 = {
    "first_name": "Matt",
    "last_name": "Murdock",
    "age": 39,
    "city": "Hell's Kitchen, NY"
}

person_3 = {
    "first_name": "Peter",
    "last_name": "Parker",
    "age": 19,
    "city": "Queens, NY"
}

people = [person_1, person_2, person_3]

for person in people:
    for field, value in person.items():
        print(f"{field.replace('_',' ').title()}: {value}")
    print("")