# #Predict the output of the following code snippets:

# 3 <= 3 < 9

# 3 == 3 == 3

# bool(0)

# bool(5 == "5")

# bool(4 == 4) == bool("4" == "4")

# bool(bool(None))

# x = (1 == True)
# y = (1 == False)
# a = True + 4
# b = False + 10

#Without print() function, the program prints nothing for the first instructions

# print("x is", x)
# print("y is", y)
# print("a:", a)
# print("b:", b)

# x is True
# y is False
# a: 5
# b: 10

# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.

#initialization of the flag at True. While it is True, the game runs.
flag = True

while flag:
    longest_sentence = input("Write the longest sentence without the lettre 'A'")

    # loop for comparing each letter in the longest sentence, if a "A" is detected, we set the flag at False,
    # Then the game stops and a message is displayed to say that a "A" is detected
    # Else, the game continues with a message counting the number of letters without "A"
    for letter in longest_sentence:
        if letter == "A":
            flag = False
    sentence_heigth = len(longest_sentence)
    if flag is True:
        print(f"Congratulations ! Your sentence contains {sentence_heigth} letters with the letter 'A'")
print("Try again ! There is a A in your sentence")

# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.
# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).
# How many sentences it contains.
# How many words it contains.
# How many unique words it contains.
# Bonus: How many non-whitespace characters it contains.
# Bonus: The average amount of words per sentence in the paragraph.
# Bonus: the amount of non-unique words in the paragraph.

sentence = "It is a sentence. It is nice."
sentence_length = len(sentence)


list_sentence_split = sentence.split()
number_words = len(list_sentence_split)
print(f"The sentence length is {sentence_length}")
print(f"There are {sentence.count(".")} sentences")
print(f"There are {number_words} words")

list_sentence_split = sentence.split()

# For searching unique words, we use a void list in which we add a word if it does not exists
# By looping through the initial sentence
# At the end, we count how much unique words are in the  list
uniqueWords = [] 
for word in list_sentence_split:
      if word not in uniqueWords:
          uniqueWords.append(word)

uniqueWordsNumber = len(uniqueWords)
print(f"There are {uniqueWordsNumber} unique word(s)")