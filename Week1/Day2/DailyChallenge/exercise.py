# Ask a user for a word.
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list, and those lists are values.

# Examples

# “dodo” ➞ { “d”: [0, 2], “o”: [1, 3] }
# “froggy” ➞ { “f”: [0], “r”: [1], “o”: [2], “g”: [3, 4], “y”: [5] }
# “grapes” ➞ { “g”: [0], “r”: [1], “a”: [2], “p”: [3] } =====> Where are the keys for letters "e" and "s" on this example ???

input_word=input("Write a word")

#Initialization of the dictionary
dict = {}

""" Looping through input_word with enumerates that splits indexes and letters of input_word
If the letter is already on the dictionary, we add the index of the letter
Else, we replace any values (here 0) by the index
At the end we print the dictionary

"""
for index, letter in enumerate(input_word):
    if letter in dict:
        dict[letter].append(index)
    else:
        dict[letter] = [index]

print(dict)