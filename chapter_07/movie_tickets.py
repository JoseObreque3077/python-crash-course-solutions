# Exercise 7-5
# A movie theater charges different ticket prices depending on a
# person’s age. If a person is under the age of 3, the ticket is free; if they
# are between 3 and 12, the ticket is $10; and if they are over age 12, the
# ticket is $15. Write a loop in which you ask users their age, and then tell
# them the cost of their movie ticket.

prompt_message = "\nHow old are you?"
prompt_message += "\nEnter 'exit' to finish.\n"

while True:
    age = input(prompt_message)
    
    if age.lower() != "exit":
        age = int(age)
    else:
        break
        
    if age < 3:
        print("\nYour ticket is free!")
    elif 3 <= age <= 12:
        print("\nYour ticket costs $10")
    else:
        print("\nYour ticket costs $15")
