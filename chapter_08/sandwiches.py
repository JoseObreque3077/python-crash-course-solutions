# Exercise 8-12
# Write a function that accepts a list of items a person wants on a
# sandwich. The function should have one parameter that collects as many items
# as the function call provides, and it should print a summary of the sandwich
# that’s being ordered. Call the function three times, using a different number
# of arguments each time.

def make_sandwich(*ingredients):
    print("Your sandwich order:")
    for ingredient in ingredients:
        print(f"-{ingredient.title()}")
        
if __name__ == "__main__":
    make_sandwich("grilled chicken", "bacon")
    make_sandwich("grilled chicken", "bacon", "mushroom")
    make_sandwich("grilled chicken", "bacon", "mushroom", "tomato")
