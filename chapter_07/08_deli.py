# Exercise 7-8
# Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop through
# the list of sandwich orders and print a message for each order, such as I
# made your tuna sandwich. As each sandwich is made, move it to the list of
# finished sandwiches. After all the sandwiches have been made, print a message
# listing each sandwich that was made.

sandwich_orders = ['grilled cheese',
                   'teriyaki chicken',
                   'roast beef',
                   'tuna',
                   'ham and cheese',
                   'vegan',
                   'BBQ']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"We are working on your {current_sandwich} sandwich order!")
    finished_sandwiches.append(current_sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()}")
