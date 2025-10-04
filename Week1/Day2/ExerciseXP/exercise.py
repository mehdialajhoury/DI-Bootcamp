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