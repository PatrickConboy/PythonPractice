# File: listComps.py
# Written by: Patrick Conboy
# Date: 9/8/2018
# Practicing with list comprehensions.

# Practice Problem 1
# Write a list comprehension that returns all numbers from 1 to 100 that produce a remainder of 3 when divided by 13.
numberList = [n for n in range(1,100) if n % 13 == 3]
print("List of all numbers 1 to 100 that give remainder 3 when divided by 13.")
print(numberList)
print("\n")

# Practice Problem 2
# Write a list comprehension that is given a list of words and appends at the end of each word a space followed by the length. So the word "art" will become "art 3".
words = ["hello", "goodbye", "slaton", "sigma", "chi"]
newWords = [word + " " + str(len(word)) for word in words]
print("List of words appended to have a space and length of word after each word.")
print(newWords)
print("\n")

# Practice Problem 3
# A string can be used as the "list" in a list comprehension, and it will then be treated as a list of its characters. 
# Use this idea to start from a string and return a list of the ASCII/UTF8 codes for the characters in the string.
testString = "hello"
print("Here are the ASCII values for the characters in 'hello'.")
print([ord(character) for character in testString])
