"""Instructions:

Use the provided Pets and Cat classes to create a Siamese breed, instantiate cat objects, and use the Pets class to manage them.
See the example below, before diving in.



Step 1: Create the Siamese Class

Create a class called Siamese that inherits from the Cat class.
You can add any specific attributes or methods for the Siamese breed, or leave it as is if there are no unique behaviors.


Step 2: Create a List of Cat Instances

Create a list called all_cats that contains instances of Bengal, Chartreux, and Siamese cats.
Example: all_cats = [bengal_obj, chartreux_obj, siamese_obj]
Give each cat a name and age.


Step 3: Create a Pets Instance

Create an instance of the Pets class called sara_pets, passing the all_cats list as an argument.


Step 4: Take Cats for a Walk

Call the walk() method on the sara_pets instance.
This should print the result of calling the walk() method on each cat in the list.
"""

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
all_cats = []

print(all_cats)

cat1 = Siamese("Niels",5)
cat2 = Chartreux("Oscar",4)
cat3 = Bengal("Piou",6)

all_cats.append(cat1)
all_cats.append(cat2)
all_cats.append(cat3)

#print(all_cats)

sara_pets = Pets(all_cats)

sara_pets.walk()

# 🌟 Exercise 2: Dogs

# Goal: Create a Dog class with methods for barking, running speed, and fighting.



# Key Python Topics:

# Classes and objects
# Methods
# Attributes


# Instructions:

# Step 1: Create the Dog Class

# Create a class called Dog with name, age, and weight attributes.
# Implement a bark() method that returns “ is barking”.
# Implement a run_speed() method that returns weight / age * 10.
# Implement a fight(other_dog) method that returns a string indicating which dog won the fight, based on run_speed * weight.


# Step 2: Create Dog Instances

# Create three instances of the Dog class with different names, ages, and weights.


# Step 3: Test Dog Methods

# Call the bark(), run_speed(), and fight() methods on the dog instances to test their functionality.


# Example (Conceptual, No Direct Solution):

# class Dog:
#     def __init__(self, name, age, weight):
#         # ... code to initialize attributes ...

#     def bark(self):
#         # ... code to return bark message ...

#     def run_speed(self):
#         # ... code to return run speed ...

#     def fight(self, other_dog):
#         # ... code to determine and return winner ...

# # Step 2: Create dog instances
# #... your code here

# # Step 3: Test dog methods
# print(dog1.bark())
# print(dog2.run_speed())
# print(dog1.fight(dog2))

class Dog():

    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f"{self.name} is barking"

    
    def run_speed(self):
        return self.weight / self.age * 10
    
    # Method which returns the winner fight of 2 dogs
    # The fight result is based on the formula run_speed() applied to a dog, and then we multiply it to its weight
    # The dog who will obtain the highest number wins the fight
    def fight(self, other_dog):
        dog1 = self.run_speed() * self.weight
        dog2 = other_dog.run_speed() * other_dog.weight
        if dog1 > dog2:
            return f"{self.name} won the figth"
        else:
            return f"{other_dog.name} won the fight"
        
# Test program :
dog1 = Dog("Bingo",15,13)
dog2 = Dog("Shana",3,30)
dog3 = Dog("Aspro",1,25)

print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(dog1.run_speed())
print(dog2.run_speed())
print(dog3.run_speed()) 

print(dog1.fight(dog2))
print(dog3.fight(dog2))
print(dog3.fight(dog1))