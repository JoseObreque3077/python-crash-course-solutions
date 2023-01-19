"""
Exercise 9-13

Make a class Die with one attribute called sides, which has a default value
of 6.
Write a method called roll_dice() that prints a random number between 1 and
the number of sides the die has. Make a 6-sided die and roll it 10 times.

Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

from random import randint


class Dice():
    """A class that represents a dice that can be rolled"""
    
    def __init__(self, sides=6):
        """Initialize the dice"""
        self.sides = sides
    
    def roll_dice(self):
        """A method that returns a random integer between 1 and 'sides'."""
        return randint(1, self.sides)
    

if __name__ == '__main__':
    dice_6 = Dice()
    dice_10 = Dice(10)
    dice_20 = Dice(20)
    
    dices = [dice_6, dice_10, dice_20]
    
    for dice in dices:
        results = []
        print(f'{dice.sides}-sided dice:')
        
        for i in range(11):
            results.append(dice.roll_dice())
            
        print(results)
