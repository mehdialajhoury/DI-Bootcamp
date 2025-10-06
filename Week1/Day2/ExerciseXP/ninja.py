"""Exercise 1: Cars

Copy the following string into your code: Volkswagen, Toyota, Ford Motor, Honda, Chevrolet.
Convert it into a list using Python (don’t do it by hand!).
Print out a message saying how many manufacturers/companies are in the list.
Print the list of manufacturers in reverse/descending order (Z-A).
Using loops or list comprehension:
Find out how many manufacturers’ names have the letter o in them.
Find out how many manufacturers’ names do not have the letter i in them.
Bonus:

There are a few duplicates in this list: ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
Remove these programmatically. (Hint: you can use a set to help you).
Print out the companies without duplicates, in a comma-separated string with no line-breaks (e.g., “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.
Bonus:

Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name."""

cars = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

cars_list = cars.split(',')

print(f"There are {len(cars_list)} car manufacturers")

# Sort all manufacturer names, then reverse the list
cars_list.sort()
print(cars_list[::-1])

counter = 0
#Count all manufacturer name which owns a "o" in their name
for name in cars_list:
    if name.find("o"):
        counter = counter + 1
print(f"There are {counter} manufacturers with a 'o' in their name")

#Count all manufacturer name which don't own a "i" in their name
for name in cars_list:
    if not name.find("i"):
        counter = counter + 1
print(f"There are {counter} manufacturers without a 'i' in their name")

cars_list = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]

#Print a set of the list : it contains only unique values
car_list_without_duplicate = list(set(cars_list))

string_cars = ""

# Looping into car_list_without_duplicate.
# For the first iteration, with only add car name, then car name with a coma separator
for car in car_list_without_duplicate:
    if string_cars != "":
        string_cars = string_cars + "," + car
    else:
        string_cars = car
print(string_cars)


print(f"There are {len(string_cars.split(','))} manufacturer names")

car_list = string_cars.split(',')

car_list.reverse
newList = [x[::-1] for x in car_list]

print(newList)

"""Exercise 2: What’s Your Name?

Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name, 3: last_name.
middle_name should be optional; if it’s omitted by the user, the name returned should only contain the first and the last name.
For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return “John Hooker Lee”.
But get_full_name(first_name="bruce", last_name="lee") will return “Bruce Lee”."""

def get_full_name(first_name,last_name,middle_name=None):
    if first_name and middle_name and last_name != "":
        return(first_name,middle_name,last_name)
    else:
        return(first_name,last_name)
    
print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))

print(get_full_name(first_name="bruce", last_name="lee"))

"""Exercise 3: From English To Morse

Write a function that converts English text to Morse code and another one that does the opposite.
Hint: Check the internet for a translation table, every letter is separated with a space and every word is separated with a slash /.
"""

morse_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    " ": "/",
}

user_input = "PYTHON IS THE GREATEST OF THE WORLD"


def convert_english_to_morse(word):

    morse_word=""
    for letter in word:
            if morse_word != "":
                morse_word = morse_word + morse_dict[letter] + " "
            else:
                 morse_word = morse_dict[letter] + " "
    if morse_word[-1] == "":
         morse_word = morse_word[:-2]
    return morse_word


def convert_morse_to_english(wordmorse):
      word_morse=""
      word=""
      reverse_morse_dict = {value: key for key, value in morse_dict.items()}

      for letter in wordmorse:
          word_morse = word_morse + letter
          if letter == " ":
            word_morse = word_morse[:-1]
            word = word + reverse_morse_dict[word_morse]
            word_morse = ""
      return word


convert = convert_english_to_morse(user_input)
print(convert)

print(convert_morse_to_english(convert))

