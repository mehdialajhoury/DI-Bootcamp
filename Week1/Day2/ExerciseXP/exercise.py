import random
# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.

# Lists:

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# Expected Output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# I use the zip function to combine 2 lists, then the dict function which converts list to dictionary
dictionary = dict(zip(keys, values))

print(dictionary)

## Write a program that calculates the total cost of movie tickets for a family based on their ages.

# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15

# Family Data:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}



# Looping on the dictionay "family" items through the key/value "member"/"age"
# Determining, according the age of each member : 
# - the cost for him for a ticket
# - the total cost incrementing while looping in each member of the family

# The program has been turned into a function in order to utilize it for the bonus part of the exercise below

def ticket_calculator(family):
    # Initialization of the total cost
    total_cost = 0
    for member, age in family.items():

        if age < 3:
            total_cost = total_cost
            print(f"it is free for {member} !")
        elif age > 3 and age <= 12:
            total_cost = total_cost + 10
            print(f"{member} has to pay 10$")
        elif age > 12:
            total_cost = total_cost + 15
            print(f"{member} has to pay 15$")
    return total_cost

total_cost = ticket_calculator(family)
print(f"The total cost for the whole family is : {total_cost}$")

# This is the bonus part of the exercise :
# Allow the user to input family members’ names and ages, then calculate the total ticket cost.

# While True (infinite loop), we ask if the player wants to add new members of the family or not
# Then, if Yes, We ask for the name and age of the new member
# The new member is added to the existing dictionary family
# We finally use the function written before to calculate the cost of the new member(s) and the whole family again

while(True):
    add_family_members = input("Do you want to add more family member(s) ? (Y/N)")
    if add_family_members == "Y":
        new_member_name = input("What is their name ?")
        new_member_age = int(input("What is their age ?"))
        family[new_member_name]=new_member_age
    else:
        break

total_cost = ticket_calculator(family)
print(f"The total cost for the whole family is : {total_cost}$")

# Create and manipulate a dictionary that contains information about the Zara brand.

# Brand Information:

# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green

# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Check if international_competitors exists and, if so, add “Desigual” to the list.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.

brand = {"name" : "Zara",
"creation_date" : 1975,
"creator_name" : "Amancio Ortega Gaona",
"type_of_clothes" : "men, women, children, home",
"international_competitors" : "Gap, H&M, Benetton",
"number_stores" : 7000,
"major_color" : {
    "France" : "blue", 
    "Spain" : "red", 
    "US" : "pink, green"}}

brand.update({"number_stores" : 2})

print(f"Zara is a brand which offers for sale some clothes for {brand["type_of_clothes"]}")

brand["country_creation"] = "Spain"

# Looping into the brand dictionary
# if the key "international_competitors" is found, adding "Desigual"
for key, value in brand.items():
  if key == "international_competitors":
    brand[key] = brand[key] + ", Desigual"

brand.pop("creation_date")
print(brand)

# Get the values of the key "international_competitors"
# Then converts into a list. Each item is separated by comas
# Finally, get the last element of the list by using [-1]

str_international_competitors = brand["international_competitors"]
list_international_competitors = str_international_competitors.split(',')

print(f"The last item of the international competitor is : {list_international_competitors[-1]}")

print(brand["major_color"]["US"])

# loop into the key brand dictionary
# count the number of key for each loop
number_of_keys = 0
for key in brand:
  number_of_keys += 1
print(f"There is {number_of_keys} keys in the dictionary 'brand'")

# print all keys in brand dictionary
for key in brand:
  print(key)

# Bonus : Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.

more_on_zara = {"creation_date" : 2025,
"number_stores" : 4}

# Using update method to merging 2 dictionaries
# The data on the first will be replaced by the second if it is the same keys
brand.update(more_on_zara)
print(brand)

# Define a function named describe_city().
# This function should accept two parameters: city and country.
# Give the country parameter a default value, such as “Unknown”.

def describe_city(city, country="Unknown"):
# Step 2: Print a Message

# Inside the function, set up the code to display a sentence like “ is in “.
# Replace <city> and <country> with the parameter values.
    print(f"{city} is in {country}")

#Step 3: Call the Function

# Call the describe_city() function with different city and country combinations.
# Try calling it with and without providing the country argument to see the default value in action.
# Example: describe_city("Reykjavik", "Iceland") and describe_city("Paris").
describe_city("Paris","France")
describe_city("London","United Kingdom")
describe_city("Berlin","Germany")

describe_city("Bamako")

describe_city("Reykjavik", "Iceland")
describe_city("Paris")


# Step 1: Import the random Module

# At the beginning of your script, use import random to access the random number generation functions.


# Step 2: Define a Function with a Parameter

# Create a function that accepts a number between 1 and 100 as a parameter.

# Step 3: Generate a Random Number

# Inside the function, use random.randint(1, 100) to generate a random integer between 1 and 100.


# Step 4: Compare the Numbers

# If they are the same, print a success message. Otherwise, print a fail message and display both numbers.

def int_accept(number):
    if 1 < number <=100:
        random_number = random.randint(1, 100)
        if number == random_number:
            print("Sucess!")
        else:
            print(f"Fail! Your number: {number}, Random number: {random_number}")
    else:
        return None
int_accept(39)


# Step 1: Define a Function with Parameters

# Define a function called make_shirt().
# This function should accept two parameters: size and text.


# Step 2: Print a Summary Message

# Set up the function to display a sentence summarizing the shirt’s size and message.


# Step 3: Call the Function



# Step 4: Modify the Function with Default Values

# Modify the make_shirt() function so that size has a default value of “large” and text has a default value of “I love Python”.


# Step 5: Call the Function with Default and Custom Values

# Call make_shirt() to make a large shirt with the default message.
# Call make_shirt() to make a medium shirt with the default message.
# Call make_shirt() to make a shirt of any size with a different message.

def make_shirt(size="large",text="I love Python"):
    print(f"the shirt size is {size} and the text is : {text}")

make_shirt(666,"Devil Inside!")

make_shirt()
make_shirt("medium")
make_shirt("small","small is the new tall")
make_shirt("extra large","Giantororus")

make_shirt(size="small", text="Hello!")


# Step 1: Create the get_random_temp() Function

# Create a function called get_random_temp() that returns a random integer between -10 and 40 degrees Celsius.


# Step 2: Create the main() Function

# Create a function called main(). Inside this function:
# Call get_random_temp() to get a random temperature.
# Store the temperature in a variable and print a friendly message like:
# “The temperature right now is 32 degrees Celsius.”


# Step 3: Provide Temperature-Based Advice

# Inside main(), provide advice based on the temperature:
# Below 0°C: e.g., “Brrr, that’s freezing! Wear some extra layers today.”
# Between 0°C and 16°C: e.g., “Quite chilly! Don’t forget your coat.”
# Between 16°C and 23°C: e.g., “Nice weather.”
# Between 24°C and 32°C: e.g., “A bit warm, stay hydrated.”
# Between 32°C and 40°C: e.g., “It’s really hot! Stay cool.”


# Step 4: Floating-Point Temperatures (Bonus)

# Modify get_random_temp() to return a random floating-point number using random.uniform() for more accurate temperature values.


# Step 5: Month-Based Seasons (Bonus)

# Instead of directly generating a random temperature, ask the user for a month (1-12) and determine the season using if/elif conditions.
# Modify get_random_temp() to return temperatures specific to each season.

# First definition of get_random_temp :
# def get_random_temp():
#     #random_integer = random.randint(-10,40)
#     return random_integer

# Second definition of get_random_temp :
# def get_random_temp():
#     random_float = random.uniform(-10,40)
#     return random_float

# Third definition of get_random_temp
def get_random_temp(season):
    if season == "Winter":
        temperature = -2
    elif season == "Spring":
        temperature = 15
    elif season == "Summer":
        temperature = 35
    elif season == "Autumn":
        temperature = 22
    return temperature

# Main was modified due to bonus exercise : an argument has been added because of the output of the month input introduced below
def main(season):
    random_temp = get_random_temp(season)
    print(f"The temperature right now is {random_temp} degrees Celsius.")
    if random_temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif random_temp >=0 and random_temp <= 16:
        print("Quite chilly! Don't forget your coat")
    elif 16 <= random_temp <= 23:
        print("Nice weather.")
    elif 24 <= random_temp <= 32:
        print("A bit warm, stay hydrated,")
    elif 32 <= random_temp <= 40:
        print("It's really hot! Stay cool.")
main("Winter")

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
print(f"The season is : {season_output}")
main(season_output)


# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

toppings = []
price=10

while(True):
    topping = input("Please write a topping would you like to your pizza. If you want to quit, type 'quit'")
    if topping == "quit":
        break
    else:
        toppings.append(topping)
        price = price + 2.50
print("This is your toppings :")
for topping in toppings:
    print(topping)
print(f"The total cost of the pizza is : {price}$")