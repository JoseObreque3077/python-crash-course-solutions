# Exercise 3-7:
# You just found out that your new dinner table won’t arrive in
# time for the dinner, and you have space for only two guests.
# Start with your program from Exercise 3-6. Add a new line
# that prints a message saying that you can invite only two
# people for dinner.
# Use pop() to remove guests from your list one at a time until
# only two names remain in your list. Each time you pop a
# name from your list, print a message to that person letting
# them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list,
# letting them know they’re still invited.
# Use del to remove the last two names from your list, so you
# have an empty list. Print your list to make sure you actually
# have an empty list at the end of your program.

guests = ["Natasha", "Scott", "Peter"]
print(f"{guests[0]}, I invite you to dinner.")
print(f"{guests[1]}, I invite you to dinner.")
print(f"{guests[2]}, I invite you to dinner.")

print("Peter can't make it!")
guests[2] = "Steve"

print(f"{guests[0]}, I invite you to dinner.")
print(f"{guests[1]}, I invite you to dinner.")
print(f"{guests[2]}, I invite you to dinner.")

print("Hi everyone! I have found a bigger table for dinner.")

guests.insert(0, "Wong")
guests.insert(2, "Peggy")
guests.append("Bruce")


print(f"{guests[0]}, I invite you to dinner.")
print(f"{guests[1]}, I invite you to dinner.")
print(f"{guests[2]}, I invite you to dinner.")
print(f"{guests[3]}, I invite you to dinner.")
print(f"{guests[4]}, I invite you to dinner.")
print(f"{guests[5]}, I invite you to dinner.")

print("I'm so sorry, I can only invite two people to dinner.")

print(f"I'm sorry {guests.pop()}, but I can't invite you to dinner.")
print(f"I'm sorry {guests.pop()}, but I can't invite you to dinner.")
print(f"I'm sorry {guests.pop()}, but I can't invite you to dinner.")
print(f"I'm sorry {guests.pop()}, but I can't invite you to dinner.")

print(f"{guests[0]}, you are still invited to dinner.")
print(f"{guests[1]}, you are still invited to dinner.")

del guests[1]
del guests[0]

print(guests)
