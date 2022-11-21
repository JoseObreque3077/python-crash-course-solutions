# Exercise 6-4
# Now that you know how to loop through a dictionary, clean up the
# code from Exercise 6-3 (page 99) by replacing your series of print() calls
# with a loop that runs through the dictionary’s keys and values. When you’re
# sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.

glossary = {
    "list": "Data structure that is a mutable ordered sequence of elements",
    "dictionary": "A collection of data values in key:value pairs",
    "tuple": "A collection of objects which ordered and immutable",
    "function": "A group of related statements that performs a specific task.",
    "loop": "Work through a collection of items, one at a time.",
    "key": "Unique data id in a dictionary",
    "value": "Key-related data value in a dictionary",
    "comment": "Comment lines in the code that are ignored by the interpreter",
    "variable": "A reserved memory location to store values",
    "string": "A series of characters"
}

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")
