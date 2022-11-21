# Exercise 8-11
# Start with your work from Exercise 8-10. Call the function
# send_messages() with a copy of the list of messages. After calling the
# function, print both of your lists to show that the original list has
# retained its messages.

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
    send_messages(messages[:], sent_messages)
    print("\nMessages:")
    show_messages(messages)
    print("\nSent Messages:")
    show_messages(sent_messages)