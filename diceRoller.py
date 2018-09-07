# File: diceRoller.py
# Written by: Patrick Conboy
# Date: 9/7/2018
# Dice rolling program that simulates one dice roll. Just made this to practice some python fundamentals.

import random

toRoll = input("Do you want to roll the die? ")

if toRoll == "yes":
    print(random.randint(1,6))