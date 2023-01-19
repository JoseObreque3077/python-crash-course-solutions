"""
Exercise 9-15

You can use a loop to see how hard it might be to win the kind
of lottery you just modeled. Make a list or tuple called my_ticket.
Write a loop that keeps pulling numbers until your ticket wins.
Print a message reporting how many times the loop had to run to give you a
winning ticket.
"""

from random import sample

def get_ticket():
    """A method that returns a ticket as a list."""
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D']
    ticket = sample(
        population=options,
        k=4
    )
    return ticket

def check_ticket(ticket, winning_ticket):
    """A method that checks if the current ticket is a winning ticket."""
    for item in ticket:
        if item not in winning_ticket:
            return False
    return True

tries = 0
max_tries = 100000
won = False

winning_ticket = get_ticket()

while not won:
    my_ticket = get_ticket()
    won = check_ticket(my_ticket, winning_ticket)
    tries += 1
    
    if tries == max_tries:
        break

if won:
    print('You win!')
    print(f'Winner Ticket: {winning_ticket}')
    print(f'Your Ticket: {my_ticket}')
    print(f'It took you {tries} attempts to win the lottery.')
else:
    print(f'You have tried {tries} attempts without winning the lottery.')
