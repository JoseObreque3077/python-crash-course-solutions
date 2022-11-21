# Exercise 8-4
# Modify the make_shirt() function so that shirts are large by default
# with a message that reads I love Python. Make a large shirt and a medium
# shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(size, message="I love Python"):
    print(f"Shirt Size: {size}")
    print(f"Message: {message}")

if __name__ == "__main__":
    make_shirt(size="L")
    make_shirt(size="M")
    make_shirt("S", "I love Java")