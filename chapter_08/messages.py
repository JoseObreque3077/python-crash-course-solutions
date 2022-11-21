# Exercise 8-9
# Make a list containing a series of short text messages. Pass the list to a
# function called show_messages(), which prints each text message.

def show_messages(messages):
    for message in messages:
        print(message)

if __name__ == "__main__":
    master_yoda_quotes = ["No! Try not. Do. Or do not. There is no try.",
                          "A Jedi's strength flows from the Force.",
                          "Luminous beings are we, not this crude matter."]
    show_messages(master_yoda_quotes)
