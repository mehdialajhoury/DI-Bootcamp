"""Instructions

Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Use List Comprehension
Example:

Suppose the following input is supplied to the program: without,hello,bag,world
Then, the output should be: bag,hello,without,world



Challenge 2 : Longest Word

Instructions

Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).
Examples

longest_word("Margaret's toy is a pretty doll.") ➞ "Margaret's"

longest_word("A thing of beauty is a joy forever.") ➞ "forever."

longest_word("Forgetfulness is by all means powerless!") ➞ "Forgetfulness"""

input_sentence = "without,hello,bag,world"

# Splitting string into a list, then sort the list
split_sentence = input_sentence.split(",")
sorted_list_sentence = sorted(split_sentence)

new_sentence=""

#List comprehension for :
# for word in sorted_list_sentence:
#     if new_sentence != "":
#         new_sentence = new_sentence+","+word
#     else:
#         new_sentence = word
new_sentence = [new_sentence+","+word if new_sentence != "" else word for word in sorted_list_sentence]
print(new_sentence)

def longest_word(sentence):
    split_sentence = sentence.split(" ")
    print(sentence)

"""Instructions

Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).
Examples

longest_word("Margaret's toy is a pretty doll.") ➞ "Margaret's"

longest_word("A thing of beauty is a joy forever.") ➞ "forever."

longest_word("Forgetfulness is by all means powerless!") ➞ "Forgetfulness"
"""

# Returns the longest word in a sentence passed as an argument
# The sentence is split, then for every word in it, we get the length
# Finally we put every word with its length in a dictionary
# We get the longest word in the dictionary using max() function combined to get
def longest_word(mysentence):
    split_sentence = mysentence.split(" ")
    dict_words = {}

    for word in split_sentence:
        dict_words[word] = len(word)

    return max(dict_words, key=dict_words.get)

# Test function

mysentence = "Margaret's toy is a pretty doll."
mysentence2 = "A thing of beauty is a joy forever."
mysentence3 = "Forgetfulness is by all means powerless!"

print(longest_word(mysentence))
print(longest_word(mysentence2))
print(longest_word(mysentence3))