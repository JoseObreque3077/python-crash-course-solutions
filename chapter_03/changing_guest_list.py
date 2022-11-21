# Exercise 3-5:
# You just heard that one of your guests can’t make the dinner,
# so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call
# at the end of your program stating the name of the guest who
# can’t make it.
# Modify your list, replacing the name of the guest who can’t
# make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person
# who is still in your list.

guests = ["Natasha", "Scott", "Peter"]
print(f"{guests[0]}, I invite you to dinner.")
print(f"{guests[1]}, I invite you to dinner.")
print(f"{guests[2]}, I invite you to dinner.")

print("Peter can't make it!")
guests[2] = "Steve"

print(f"{guests[0]}, I invite you to dinner.")
print(f"{guests[1]}, I invite you to dinner.")
print(f"{guests[2]}, I invite you to dinner.")
