import random
from statistics import mean

"""Exercise 1: Birthday Look-Up

Create a variable called birthdays. Its value should be a dictionary.
Initialize this variable with the birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip: Use the format "YYYY/MM/DD".
Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”
Ask the user to give you a person's name and store the answer in a variable.
Get the birthday of the name provided by the user.
Print out the birthday with a nicely-formatted message."""

birthdays = {"Steve Jobs" : "1955/02/24",
             "Shigeru Miyamoto" : "1952/11/16",
             "Hideo Kojima" : "1963/08/24",
             "Gabe Newell" : "1962/11/3",
             "Elon Musk" : "1971/06/28"            
             }
print("Welcome Here ! You can look up the birthdays of the people in the list !")

for name, birthday in birthdays.items():
    print(name)

user_input = input("Choose one please")

for name, birthday in birthdays.items():
    if name == user_input:
        birthday_out = birthday

print(f"{user_input} was born on the : {birthday_out}")

"""Exercise 2: Birthdays Advanced

Before asking the user to input a person's name, print out all of the names in the dictionary.
If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the birthday information for person's name”).
"""

print("Welcome Here ! You can look up the birthdays of the people in the list !")

for name, birthday in birthdays.items():
    print(name)

user_input = input("Choose one please")

for name, birthday in birthdays.items():
    if name == user_input:
        person_found = True
        birthday_out = birthday
    else :
        person_found = False

if person_found:
    print(f"{user_input} was born on the : {birthday_out}")
else:
    print(f"Sorry, we don’t have the birthday information for {user_input}")


"""Exercise 3: Check The Index

Instructions

Using this variable

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
Ask a user for their name, if their name is in the names list, print out the index of the first occurence of the name.

Example: if input is 'Cortana' we should be printing the index 1"""

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_input = "Cortana"


for name in names:
    if name == user_input:
        index = names.index(name)
print(f"The index of {user_input} is {index}")



"""Exercise 4: Double Dice

Create a function that will simulate the rolling of a dice. Call it throw_dice. It should return an integer between 1 and 6.
Create a function called throw_until_doubles.
It should keep throwing 2 dice (using your throw_dice function) until they both land on the same number, i.e., until we reach doubles.
For example: (1, 2), (3, 1), (5, 5) → then stop throwing, because doubles were reached.
This function should return the number of times it threw the dice in total. In the example above, it should return 3.
Create a main function. It should throw doubles 100 times (i.e., call your throw_until_doubles function 100 times), and store the results of those function calls (in other words, how many throws it took until doubles were thrown, each time) in a collection. (What kind of collection? Read below to understand what we will need the data for, and this should help you decide which data structure to use).
After the 100 doubles are thrown, print out a message telling the user how many throws it took in total to reach 100 doubles.
Also print out a message telling the user the average amount of throws it took to reach doubles. Round this off to 2 decimal places.
For example:

If the results of the throws were as follows (your code would do 100 doubles, not just 3):

(1, 2), (3, 1), (5, 5)
(3, 3)
(2, 4), (1, 2), (3, 4), (2, 2)
Then my output would show something like this:

Total throws: 8
Average throws to reach doubles: 2.67."""

list_throw = []

def throw_dice():
    return random.randint(1,6)

# Functions loops until a break appears. We throws 2 dices and stock the result in a list of tuples.
# If the throw1 equals the throw2, it breaks the loop and give in return the number of tries.
def throw_until_doubles():
    count_throw = 0
    while(True):
        throw1 = throw_dice()
        throw2 = throw_dice()
        tuple_throw = (throw1,throw2)
        list_throw.append(tuple_throw)
        count_throw +=1
        if throw1 == throw2:
            break
    
    return count_throw

list_avg = []

# Main function : it will throw 100 times the function throw_uuntil_doubles()
# Returns the total of tries to reach 100 doubles and a list with the number of tries to have a double for each try

def main():
    total = 0
    for throw in range(1,100):
        total = total + throw_until_doubles()
        count = throw_until_doubles()
        list_avg.append(count)
    return total,list_avg


result = main()
list_throw = result[1]
# Utilization of the mean() function from the statistics module which returns an average from a list
list_avg = mean(list_avg)
total_throws = result[0]

print(f"Total throws : {total_throws}")
print(f"Average throws to reach doubles: {list_avg}")