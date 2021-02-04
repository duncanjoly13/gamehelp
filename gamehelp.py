# GAMEHELP v 1.0
# a game assistance module with
# coin flips, dice, and cards
# created by Duncan Joly on March 31 April 1 2017

__version__ = 1.0

import random

#flip coin, prints
def flip():
    sides = ["heads", "tails"]
    choice = random.choice(sides)
    return choice

def roll(sides, numberofDice = 1):
    num = random.randint(numberofDice, sides*numberofDice)
    return num

def deal(numOfCards):
    suits = ["hearts", "spades", "diamonds", "clubs"]
    numbers = ["ace", "2", "3", "4",
               "5", "6", "7", "8", "9",
               "10", "jack", "queen", "king"]
    for i in range(cards):
        suit = random.choice(suits)
        number = random.choice(numbers)
        return number + " of " + suit

def spin(n):
	spun = random.randint(1, n)
	return spun
    
