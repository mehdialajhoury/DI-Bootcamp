#Print the following output in one line of code:
print("Hello world \nHello World\nHello World\nHello World")

#Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).
result = (99^3)*8
print(result)

#Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.
name = input("What is your name")

if name == "Mehdi":
    print("LOL we have the same name xD")
else:
    print("Argh, what a boring name...")

#Write code that will ask the user for their height in centimeters.

centimeter_user = input("How height are you ? (In centimeters)")
if int(centimeter_user) > 145:
    print("You are enough tall to ride. Enjoy !")
else:
    print("You need to grow more to ride !")

#Create a set called my_fav_numbers and populate it with your favorite numbers.
#Add two new numbers to the set.
#Remove the last number you added to the set.
#Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
#Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {8, 32, 64, 128}
my_fav_numbers.add(256)
my_fav_numbers.add(512)
print(my_fav_numbers)

my_fav_numbers.remove(512)

friend_fav_numbers = {1, 2, 56, 25}

concatenate_sets = my_fav_numbers.union(friend_fav_numbers)
print(concatenate_sets)

#Given a tuple of integers, try to add more integers to the tuple.
#Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.

integer_tuples = (12,24,54,34)

#In the line below, we can't add something to a tuple because it is immutable
#integer_tuples.__add__(24)

#You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#Remove "Banana" from the list.
#Remove "Blueberries" from the list.
#Add "Kiwi" to the end of the list.
#Add "Apples" to the beginning of the list.
#Count how many times "Apples" appear in the list.
#Empty the list.
#Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.append("Apples")

print(basket)
print(basket.count("Apples"))
basket.clear()
print(basket)

#Using the list below :

#sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"].

#The deli has run out of pastrami, use a while loop to remove all occurrences of Pastrami sandwich from sandwich_orders.
#We need to prepare the orders of the clients:

#Create an empty list called finished_sandwiches.

#One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
#After all the sandwiches have been made, print a message listing each sandwich that was made, such as:

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)

finished_sandwiches=[]

sandwich_orders_copy=sandwich_orders.copy()

for sandwich in sandwich_orders_copy:
    finished_sandwiches.append(sandwich)
    sandwich_orders.remove(sandwich)

print(sandwich_orders)
print(finished_sandwiches)

