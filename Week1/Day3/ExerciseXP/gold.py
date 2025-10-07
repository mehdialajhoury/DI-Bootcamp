import math
import random

"""Exercise 1 : Geometry

Instructions

Write a class called Circle that receives a radius as an argument (default is 1.0).
Write two instance methods to compute perimeter and area.
Write a method that prints the geometrical definition of a circle."""

class Circle:

    def __init__(self,radius=1.0):
        self.radius = radius

    def permiter(self):
        return 2*math.pi*self.radius
    
    def area(self):
        return (math.pi.radius)**2


"""Exercise 2 : Custom List Class

Instructions

Create a class called MyList, the class should receive a list of letters.
Add a method that returns the reversed list.
Add a method that returns the sorted list.
Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension)."""

class MyList():
    def __init__(self,letters_list):
        self.letters_list = letters_list

    def reversed_list(self):
        return reversed(self.letters_list)
    
    def sorted_list(self):
        return sorted(self.letters_list)
    
    def second_list(self):
        second_list = []
        length_list = len(self.letters_list)
        for i in range(0,length_list):
            second_list.append(random.randint(1,10))
        return second_list

#Test program :

list_letters = ['b','o','n','j','o','u','r']
mylist = MyList(list_letters)
print(mylist.second_list())


"""Exercise 3 : Restaurant Menu Manager

Instructions

The purpose of this exercise is to create a restaurant menu. The code will allow a manager to add and delete dishes.

Create a python file called menu_manager.py.

Create a class called MenuManager.

Create a method __init__ that instantiates an attribute called menu. The menu attributes value will be all the current dishes (list of dictionaries). Each dish will be stored in a dictionary where the keys are name, price, spice level and gluten index (which value is a boolean).

Here is a list of the dishes currently on the menu:

    Soup – 10 – B - False
    Hamburger – 15 - A - True
    Salad – 18 - A - False
    French Fries – 5 - C - False
    Beef bourguignon– 25 - B - True

    Meaning: For the spice level:
       • A = not spicy,
       • B = a little spicy,
       • C = very spicy


The dishes provided above should be the value of the menu attribute.

Create a method called add_item(name, price, spice, gluten). This method will add new dishes to the menu.

Create a method called update_item(name, price, spice, gluten). This method checks whether a dish is in the menu, if the dish exists then update it. If not notify the manager that the dish is not in the menu.

Create a method called remove_item(name). This method should check if the dish is in the menu, if the dish exists then delete it and print the updated dictionary. If not notify the manager that the dish is not in the menu."""

class MenuManager():
    
    def __init__(self):
        self.menu = []

    def add_item(self,name, price, spice, gluten):
        dict_dishes = {}
        dict_dishes["name"] = name
        dict_dishes["price"] = price
        dict_dishes["spice"] = spice
        dict_dishes["gluten"] = gluten
        self.menu.append(dict_dishes)
        #print(dict_dishes)

    def update_item(self,name, price, spice, gluten):
        for dish in self.menu:
            #print(dish)
            if name in dish["name"]:
                dish["price"] = price
                dish["spice"] = spice
                dish["gluten"] = gluten
                print(f"{dish["name"]} dish has been updated")
            else:
                print("This dish doesn t exists")

    def remove_item(self,name):
        for dish in self.menu:
            if name in dish["name"]:
                dish.pop('name')
                print(f"{name} has been deleted")
            else:
                print("This dish doesn't exists")
        print(dish)

menu = MenuManager()
menu.add_item("Soup",10,"B",False)
menu.add_item("Steak",5,"A",False)
menu.update_item("Pizza",15,"C",True)
menu.update_item("Steak",10,"A",False)
menu.remove_item("Steak")