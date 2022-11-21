# Exercise 7-2
# Write a program that asks the user how many people are in
# their dinner group. If the answer is more than eight, print a message saying
# they’ll have to wait for a table. Otherwise, report that their table is ready.

party_size = int(input("Hi, How many people are in your dinner group? "))

if party_size > 8:
    print("Sorry, we are full house tonight. You'll have to wait for a table.")
else:
    print("Welcome! Your table is ready.")
