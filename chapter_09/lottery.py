"""
Exercise 9-14

Make a list or tuple containing a series of 10 numbers and five letters.
Randomly select four numbers or letters from the list and print a message
saying that any ticket matching these four numbers or letters wins a prize.
"""

from random import sample

options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D']

winner_ticket = sample(
    population=options,
    k=4
)

print('Any ticket matching these four numbers or letters wins a prize:')
print(winner_ticket)
