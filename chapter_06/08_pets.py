# Exercise 6-8
# Make several dictionaries, where each dictionary represents a different pet.
# In each dictionary, include the kind of animal and the owner’s name. Store
# these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.

pet_1 = {
    "name": "mickey",
    "type": "mouse",
    "age": 1,
    "owner": "walt"
}

pet_2 = {
    "name": "monty",
    "type": "python",
    "age": 2,
    "owner": "guido"
}

pet_3 = {
    "name": "buggs",
    "type": "rabbit",
    "age": 3,
    "owner": "tex"
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"\n{pet['name'].title()}'s Info: ")
    for field, value in pet.items():
        print(f"{field.title()}: {value}")
