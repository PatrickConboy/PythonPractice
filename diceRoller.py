# File: diceRoller.py
# Written by: Patrick Conboy
# Date: 9/7/2018
# Dice rolling program that simulates one dice roll. Just made this to practice some python fundamentals.

import random

toRoll = input("Do you want to roll the dice? ")

die1 = 0
die2 = 0
if toRoll == "yes" or toRoll == "Yes" or toRoll == "YES":
    sumDie = 0
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    sumDie = die1 + die2
    print("You rolled a " + str(die1) + " and a " + str(die2) + ", for a total of " + str(sumDie) + ".")

if toRoll == "no" or toRoll == "No" or toRoll == "NO":
    print("Then why are you wasting my time?")