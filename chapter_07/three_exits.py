# Exercise 7-6
# Write different versions of either Exercise 7-4 or Exercise 7-5 that do
# each of the following at least once:
# Use a conditional test in the while statement to stop the loop.
# Use an active variable to control how long the loop runs.
# Use a break statement to exit the loop when the user enters a 'quit' value.

# Note: Source code from exercise 7-4

prompt_message = "\nWhat kind of pizza toppings do you want?"
prompt_message += "\nType 'exit' to finish.\n"

# Case 1: Using a conditional test
topping = ""
while topping != "exit":
    topping = input(prompt_message).lower()
    
    if topping != "exit":
        print(f"\nI'll add {topping} to your pizza.")
        
# Case 2: Using an active variable
flag = True
while flag:
    topping = input(prompt_message).lower()
    
    if topping != "exit":
        print(f"\nI'll add {topping} to your pizza.")
    else:
        flag = False
    

# Case 3: Using a break statement
while True:
    topping = input(prompt_message).lower()
    
    if topping == "exit":
        break
    else:
        print(f"\nI'll add {topping} to your pizza.")
