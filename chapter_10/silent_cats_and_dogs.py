"""
Exercise 10-9

Modify your except block in Exercise 10-8 to fail silently if either file
is missing.
"""

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as file:
            file_contents = file.read()
    except FileNotFoundError:
        pass
    else:
        print(f'File: {filename}')
        print(file_contents + '\n')
