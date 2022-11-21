# Exercise 6-12
# We’re now working with examples that are complex enough that they
# can be extended in any number of ways. Use one of the example programs from
# this chapter, and extend it by adding new keys and values, changing the
# context of the program or improving the formatting of the output.

# Source code from exercise 6-1

person = {
    "first_name": "José",
    "last_name": "Alarcon",
    "age": 26,
    "city": "Temuco"
}

for field, value in person.items():
    print(f"{field.replace('_', ' '). title()}: {value}")
