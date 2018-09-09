# File: listComps.py
# Written by: Patrick Conboy
# Date: 9/8/2018
# Practicing with list comprehensions.

# Practice Problem 1
# Write a list comprehension that returns all numbers from 1 to 100 that produce a remainder of 3 when divided by 13.
numberList = [n for n in range(1,100) if n % 13 == 3]
print(numberList)

# Practice Problem 2
# Write a list comprehension that is given a list of words and appends at the end of each word a space followed by the length. So the word "art" will become "art 3".
words = ["hello", "goodbye", "slaton", "sigma", "chi"]
newWords = [word + " " + str(len(word)) for word in words]
print(newWords)

