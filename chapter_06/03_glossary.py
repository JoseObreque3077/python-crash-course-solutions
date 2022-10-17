# Exercise 6-3
# A Python dictionary can be used to model an actual dictionary. However,
# to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the
# previous chapters. Use these words as the keys in your
# glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output.
# You might print the word followed by a colon and then its
# meaning, or print the word on one line and then print its
# meaning indented on a second line. Use the newline character
# (\n) to insert a blank line between each word-meaning pair in
# your output.

glossary = {
    "list": "Data structure that is a mutable ordered sequence of elements",
    "dictionary": "Data structure that are used to store data values in key:value pairs",
    "tuple": "A tuple is a collection of objects which ordered and immutable",
    "function": "A function is a group of related statements that performs a specific task.",
    "loop": "Work through a collection of items, one at a time."
}

print(f"List: {glossary['list']}")
print(f"\nDictionary: {glossary['dictionary']}")
print(f"\nTuple: {glossary['tuple']}")
print(f"\nFunction: {glossary['function']}")
print(f"\nLoop: {glossary['loop']}")
