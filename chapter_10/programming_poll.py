"""
Exercise 10-5

Write a while loop that asks people why they like programming. Each time
someone enters a reason, add their reason to a file that stores all the
responses.
"""
filename = 'programming_poll.txt'

poll_responses = []

while True:
    response = input('\nWhy do you like programming? ')
    poll_responses.append(response)
    
    continue_poll = input('Would you like to continue with the poll? (Y/N) ')
    
    if continue_poll.upper() == 'N':
        break

with open(filename, 'a') as file:
    for response in poll_responses:
        file.write(f'{response}\n')
