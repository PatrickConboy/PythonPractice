# File: diceGame.py
# Written by: Patrick Conboy
# Date: 9/7/2018
# This program simulates a quick guessing game of a dice roll. 
# The user guesses even or odd and the game tells them if they won or not.

import random

userGuess = input("Call it, even or odd? ")

die1 = 0
die2 = 0
sumDie = 0

die1 = random.randint(1,6)
die2 = random.randint(1,6)
sumDie = die1 + die2
print("The roll is " + str(die1) + " and " + str(die2) + ", for a total of " + str(sumDie) + ".")

if sumDie % 2 == 0 and userGuess == "even" or sumDie % 2 != 0 and userGuess == "odd":
    print("You win. Nice job, kid.")

else:
    print("You lose. Tough luck, kid.")

