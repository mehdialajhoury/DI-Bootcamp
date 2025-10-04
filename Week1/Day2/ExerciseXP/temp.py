# import random
# Step 1: Import the random Module

# At the beginning of your script, use import random to access the random number generation functions.


# Step 2: Define a Function with a Parameter

# Create a function that accepts a number between 1 and 100 as a parameter.

def int_accept(number):
    if 1 < number <=100:
        print("good")
    else:
        return None

int_accept(101)