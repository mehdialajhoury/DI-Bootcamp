import random

# Ask the user to input a month (1 to 12).
# Display the season of the month received:
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)


month_input = int(input("Choose a month between 1 and 12"))

#List of all Seasons according the number of the month
season_list = ["Winter","Winter","Spring","Spring","Spring","Summer","Summer","Summer","Autumn","Autumn","Autumn","Winter"]

season_list_length = len(season_list)

#Loop into all month of the seasons. We add one, accordingly to the loop for which is exclusive
#If the number of the month in input equals to the index of the season list, we pick the season corresponding to the the index list minus 1 because and the index of the list go from 0 to 11
for season in range(1, season_list_length + 1):
    if month_input == season:
        season_output = season_list[season-1]
print(season_output)


# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

#loop printing all numbers from 1 to 20
for number in range(1,21):
    print(number)

#loop printing all the numbers (in a range from 1 to 20) that have a rest of 0 if they are divided by 2 (even)
for number in range(1,21):
    if number % 2 == 0:
        print(number)

# Write a while loop that keeps asking the user to enter their name.
# Stop the loop if the user’s input is your name.

name = ""
while name != "Mehdi":
    name = input("Write your name")

# Using this variable:

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# Ask a user for their name, if their name is in the names list print out the index of the first occurrence of the name.

# Example: if input is Cortana we should be printing the index 1

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name_input = input("Write your name")

# If the input name is in the list of names, we continue, else, the program stops
# For the name who is in the list, we store the first occurence of the index in a string, and then we print it

if name_input in names:
    for name in names:
        if name == name_input:
            name_output = names.index(name)
    print(name_output)
else:
    print("Sorry ! Your name is not in the list !")

#Ask the user for 3 numbers and print the greatest number

first_number = int(input("Choose a 1st number"))
second_number = int(input("Choose a 2nd number"))
third_number = int(input("Choose a 3rd number"))

# Comparison between all inputs. It prints the greatest number
if first_number > second_number and first_number > third_number:
    print(first_number)
elif second_number > first_number and second_number > third_number:
    print(second_number)
else:
    print(third_number)


# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says “Winner”.
# If the user guesses the wrong number print a message that says “Better luck next time.”
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop, tally up and display total games won and lost.


# nombremagique = random.randrange(1,100)

# for i in range(0,7):
#     entree_utilisateur=input("Choisissez un nombre parmi 1 et 100. Vous avez 7 tentatives !")
#     if int(entree_utilisateur) >=1 and int(entree_utilisateur) <=100:
#         if entree_utilisateur != nombremagique:
#             if int(entree_utilisateur) > nombremagique:
#                 print("C'est moins !")
#             else:
#                 print("C'est plus !")
#         else:
#             print("BRAVO !! Vous avez deviné !")
#             break
#     else:
#         print("Vous devez choisir un nombre entre 1 et 100 !!!")
# print("Le nombre magique était :"+str(nombremagique))

# Random number generation using random module
random_number = random.randrange(1,10)

# Variables initialization : flag is True while the game runs, if the user choose "n" after a play, the game stops
# lost_number, win_number : counts all the games the play has won / lost and display them at the end of the game
flag=True
lost_number=0
win_number=0

# While the game runs, the flag is true.
# The random number is reinitialized if the player won and wants to continue to play

while flag:
    input_number = int(input("Choose a number from 1 to 9 !"))
    if input_number == random_number:
        print("Winner")
        win_number +=1
        keep_guessing = input("Continue ? (y/n)")
        if keep_guessing == "y":
            random_number = random.randrange(1,10)
            flag=True
        elif keep_guessing == "n":
            flag=False
    else:
        print("Better luck next time")
        lost_number +=1
        keep_guessing = input("Continue ? (y/n)")
        if keep_guessing == "y":
            flag=True
        elif keep_guessing == "n":
            flag=False

print(f"total won : {win_number} / total lost : {lost_number} ")