# Exercise 8-10
# Start with a copy of your program from Exercise 8-9. Write a
# function called send_messages() that prints each text message and moves each
# message to a new list called sent_messages as it’s printed. After calling the
# function, print both of your lists to make sure the messages were moved
# correctly.

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)

if __name__ == "__main__":
    messages = ["Hello Python!", "Hello Java!", "Hello Ruby!"]
    sent_messages = []
    send_messages(messages, sent_messages)
    print("\nMessages:")
    show_messages(messages)
    print("\nSent Messages:")
    show_messages(sent_messages)
