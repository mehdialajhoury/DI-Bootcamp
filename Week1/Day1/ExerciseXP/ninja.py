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