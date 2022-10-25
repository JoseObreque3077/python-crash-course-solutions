# Exercise 7-10
# Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where
# would you go? Include a block of code that prints the results of the poll.

results = {}

while True:
    name = input("\nWhat is your name? ").title()
    place = input("Where would you go on your dream vacation? ").title()
    
    results[name] = place
    
    repeat_poll = input("Will you continue adding answers? (yes/no) ").lower()
    
    if repeat_poll == "no":
        break

print("\nPoll Results:")
for name, place in results.items():
    print(f"{name} wants to go to {place}")
