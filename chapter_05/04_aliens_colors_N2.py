# Exercise 5-4
# Choose a color for an alien as you did in Exercise 5-3, and write
# an if-else chain.
# - If the alien’s color is green, print a statement that the player
#   just earned 5 points for shooting the alien.
# - If the alien’s color isn’t green, print a statement that the
#   player just earned 10 points.
# - Write one version of this program that runs the if block and
#   another that runs the else block.

# VERSION 1:
alien_color = "green"
if alien_color == "green":
    print("You earn 5 points for shooting the alien!")
else:
    print("You earn 10 points!")

# VERSION 2:
alien_color = "red"
if alien_color == "green":
    print("You earn 5 points for shooting the alien!")
else:
    print("You earn 10 points!")
