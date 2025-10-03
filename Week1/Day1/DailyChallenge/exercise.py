#Ask the user for a number and a length.

#Create a program that prints a list of multiples of the number until the list length reaches length.

number = int(input("Choose a number"))
length = int(input("Choose a length"))

multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)
print(multiples)

#Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

string_user = input("Write a string")

#Initialization of a list which be compared with the string in input :
#We put the first letter of the string input in a list in order to compare it when the first loop will start

result_list = [string_user[0]]

#We can loop from the beginning of the string until the last occurence of it
#Then, we compare the lettre with previous one, and if we don't see the same, we add it to a result_list
#Finally, we convert this list to a new string with the join() method
for i in range(1, len(string_user)):
        if string_user[i] != string_user[i - 1]:
            result_list.append(string_user[i])
new_string = "".join(result_list)

print(new_string)