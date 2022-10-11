# Exercise 3-6:
# You just found a bigger dinner table, so now more space is available.
# Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or Exercise 3-5.
# Add a print() call to the end of your program informing
# people that you found a bigger dinner table.
# Use insert() to add one new guest to the beginning of your
# list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in
# your list.

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
