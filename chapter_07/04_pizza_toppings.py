# Exercise 7-4
# Write a loop that prompts the user to enter a series of pizza
# toppings until they enter a 'quit' value. As they enter each topping, print
# a message saying you’ll add that topping to their pizza.

prompt_message = "\nWhat kind of pizza toppings do you want?"
prompt_message += "\nType 'exit' to finish.\n"

while True:
    topping = input(prompt_message)
    
    if topping.lower() == "exit":
        break
    else:
        print(f"\nI'll add {topping.lower()} to your pizza.")
