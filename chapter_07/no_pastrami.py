# Exercise 7-9
# Using the list sandwich_orders from Exercise 7-8, make sure the
# sandwich 'pastrami' appears in the list at least three times. Add code near
# the beginning of your program to print a message saying the deli has run out
# of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in
# finished_sandwiches.

sandwich_orders = ['pastrami',
                   'grilled cheese',
                   'teriyaki chicken',
                   'pastrami',
                   'roast beef',
                   'tuna',
                   'pastrami',
                   'ham and cheese',
                   'vegan',
                   'BBQ']
finished_sandwiches = []

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"We are working on your {current_sandwich} sandwich order!")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")
