# Exercise 5-9
# Add an if test to hello_admin.py to make sure the list of users is not
# empty.
# If the list is empty, print the message We need to find some users!
# Remove all of the usernames from your list, and make sure
# the correct message is printed.

usernames = []

if len(usernames) == 0:
    print("We need to find some users!")
else:
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again")
