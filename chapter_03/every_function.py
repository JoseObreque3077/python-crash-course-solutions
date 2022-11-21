# Exercise 3-10:
# Think of something you could store in a list. For example, you
# could make a list of mountains, rivers, countries, cities, languages, or anything else
# you’d like. Write a program that creates a list containing these items and then uses each
# function introduced in this chapter at least once.

languages = ["Java", "Python"]

# Adding elements
languages.insert(0, "Dart")
languages.append("Kotlin")
languages.append("C#")
languages.append("JavaScript")

# Removing elements
languages.pop(0)
languages.remove("JavaScript")

# Creating new sorted lists
languages_sorted = sorted(languages)
languages_reverse_sorted = sorted(languages, reverse=True)
print(languages_sorted)
print(languages_reverse_sorted)

# Sort original list
languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)

# Original list length
print(len(languages))
