from datetime import date, timedelta

# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

birthday_input = input("What is your birthdate ? (Please use the format DD/MM/YYYY)")

# convert string birthday input into a date YYYY/MM/DD
birthday = date(int(birthday_input[6:10]),int(birthday_input[3:5]),int(birthday_input[0:2]))

# get today date
today = date.today()

# calc age = today - birhday 
age = (today - birthday) // timedelta(days=365.2425)

age_to_string = str(age)

#get the last number of age in input and convert to int
last_number_age = age_to_string[1]
last_number_age = int(last_number_age)

# Initializing the list of the candle at the top of the cake
candle_list = ""

# If the number does not contains 0, we add a candle (represented by "i" letter) each time we loop through the last number age
# Else, we add directly 10 "_" : no candle at the top of the cake
if last_number_age != 0:
    for i in range(1,last_number_age + 1):
        candle_list = candle_list + "i"
    how_much_underscores_to_add = 10 - len(candle_list)
    candle_list = candle_list + how_much_underscores_to_add*"_"
elif last_number_age == 0:
    candle_list = ("__________")

# Printing the cake :

print("    "+candle_list)
print("   |:H:a:p:p:y:|")
print(" __|___________|__")
print("|^^^^^^^^^^^^^^^^^|")
print("|:B:i:r:t:h:d:a:y:|")
print("|                 |")
print("~~~~~~~~~~~~~~~~~~~")