# Exercice 5-2
# More Conditional Tests: You don’t have to limit the number of tests you create
# to ten. If you want to try more comparisons, write more tests and add them to
# conditional_tests.py. Have at least one True and one False result for each of
# the following:
# - Tests for equality and inequality with strings
# - Tests using the lower() method
# - Numerical tests involving equality and inequality, greater
#   than and less than, greater than or equal to, and less than or
#   equal to
# - Tests using the and keyword and the or keyword
# - Test whether an item is in a list
# - Test whether an item is not in a list

print("Tests for inequality and equality with strings")
print(f"Is 'potato' = 'potato'? Answer: {'potato' == 'potato'}")
print(f"Is 'hola' = 'mundo'? Answer: {'hola' == 'mundo'}")
print(f"Is 'potato' not equal to 'carrot'? Answer: {'potato' != 'carrot'}")
print(f"Is 'hola' not equal to 'hola'? Answer: {'hola' != 'hola'}")

print("\nTests using lower() method")
print(f"is 'Alfa'.lower() = 'alfa'? Answer: {'Alfa'.lower() == 'alfa'}")
print(f"is 'Beta'.lower() = 'Beta'? Answer: {'Beta'.lower() == 'Beta'}")

print("\nNumerical tests")
print(f"Is 5 = 5?: Answer: {5 == 5}")
print(f"Is 10 = 15? Answer: {10 == 15}")
print(f"Is 96 not equal to 69?: Answer: {96 != 69}")
print(f"Is 1 not equal to 1? Answer: {1 != 1}")
print(f"Is 40 < 105.55? Answer: {40 < 105.55}")
print(f"Is 250.42 < 105.55? Answer: {250.42 < 105.55}")
print(f"Is 400 > 100? Answer: {400 > 100}")
print(f"Is 42.4545 > 89.3434? Answer: {42.4545 > 89.3434}")
print(f"Is 150 >= 150? Answer: {150 >= 150}")
print(f"Is 3.14 >= 6.28? Answer: {3.14 >= 6.28}")
print(f"Is 150 <= 350? Answer: {150 <= 350}")
print(f"Is 1000 <= 990? Answer: {1000 <= 990}")

print("\nTests using the and keyword and the or keyword")
print(f"Is 5 > 1 and 10 <= 20? Answer: {5>1 and 10<=20}")
print(f"Is 'dog' = 'cat' and 2+2 = 4 ? Answer: {'dog' == 'cat' and 2+2 == 4}")
print(f"Is 5 < 1 or 10 <= 20? Answer: {5<1 or 10<=20}")
print(f"Is 'dog' = 'cat' or 2+2 = 5 ? Answer: {'dog' == 'cat' or 2+2 == 5}")

print("\nTests items in list")
print(f"Is 9 in [3,6,9,12,15]? Answer: {9 in [3, 6, 9, 12, 15]}")
print(f"Is 18 in [3,6,9,12,15]? Answer: {18 in [3, 6, 9, 12, 15]}")

print("\nTests items not in list")
print(f"Is 5 not in [3,6,9,12,15]? Answer: {5 not in [3, 6, 9, 12, 15]}")
print(f"Is 9 not in [3,6,9,12,15]? Answer: {9 not in [3, 6, 9, 12, 15]}")
