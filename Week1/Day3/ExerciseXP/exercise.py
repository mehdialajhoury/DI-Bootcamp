"""Instructions:

Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.



Step 1: Create Cat Objects

Use the Cat class to create three cat objects with different names and ages.


Step 2: Create a Function to Find the Oldest Cat

Create a function that takes the three cat objects as input.
Inside the function, compare the ages of the cats to find the oldest one.
Return the oldest cat object.


Step 3: Print the Oldest Cat’s Details

Call the function to get the oldest cat.
Print a formatted string: “The oldest cat is <cat_name>, and is <cat_age> years old.”
Replace <cat_name> and <cat_age> with the oldest cat’s name and age.
"""

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

    # Step 1: Create cat objects
    # cat1 = create the object

    # Step 2: Create a function to find the oldest cat
    def find_oldest_cat(cat1, cat2, cat3):
        if cat1.age > cat2.age and cat1.age > cat3.age:
            return cat1
        elif cat2.age > cat1.age and cat2.age > cat3.age:
            return cat2
        else:
            return cat3
        
        # ... code to find and return the oldest cat ...

    # Step 3: Print the oldest cat's details

cat1 = Cat("Piou",6)
cat2 = Cat("Niels",7)
cat3 = Cat("Oscar",8)

oldest_cat = Cat.find_oldest_cat(cat1,cat2,cat3)
print(f"The oldest cat is {oldest_cat.name} and is {oldest_cat.age}")


"""🌟 Exercise 2 : Dogs

Goal: Create a Dog class, instantiate objects, call methods, and compare dog sizes.



Key Python Topics:

Classes and objects
Object instantiation
Methods
Attributes
Conditional statements (if)


Instructions:

Create a Dog class with methods for barking and jumping. Instantiate dog objects, call their methods, and compare their sizes.



Step 1: Create the Dog Class

Create a class called Dog.
In the __init__ method, take name and height as parameters and create corresponding attributes.
Create a bark() method that prints “ goes woof!”.
Create a jump() method that prints “ jumps cm high!”, where x is height * 2.


Step 2: Create Dog Objects

Create davids_dog and sarahs_dog objects with their respective names and heights.


Step 3: Print Dog Details and Call Methods

Print the name and height of each dog.
Call the bark() and jump() methods for each dog.
"""

class Dog():
    def __init__(self, name,height):
        self.name = name
        self.height = height

    def bark(self):
        print("goes woof!")

    def jump(self):
        print(f"jumps {self.height*2} cm")

davids_dog = Dog("Bingo",60)
sarahs_dog = Dog("Ralfo",110)

print(davids_dog.name,davids_dog.height)
print(sarahs_dog.name,sarahs_dog.height)

davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()

"""🌟 Exercise 3 : Who’s The Song Producer?

Goal: Create a Song class to represent song lyrics and print them.



Key Python Topics:

Classes and objects
Object instantiation
Methods
Lists


Instructions:

Create a Song class with a method to print song lyrics line by line.



Step 1: Create the Song Class

Create a class called Song.
In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.


Example:

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"]

"""

class Song():
    def __init__(self,lyrics):

        self.lyrics = lyrics

    def sing_me_a_song(self):
        for lyric in self.lyrics:
            print(lyric)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()



"""🌟 Exercise 4 : Afternoon At The Zoo

Goal:

Create a Zoo class to manage animals. The class should allow adding animals, displaying them, selling them, and organizing them into alphabetical groups.



Key Python Topics:

Classes and objects
Object instantiation
Methods
Lists
Dictionaries (for grouping)
String manipulation


Instructions

Step 1: Define The Zoo Class

1. Create a class called Zoo.

2. Implement the __init__() method:

It takes a string parameter zoo_name, representing the name of the zoo.
Initialize an empty list called animals to keep track of animal names.
3. Add a method add_animal(new_animal):

This method adds a new animal to the animals list.
Do not add the animal if it is already in the list.
4. Add a method get_animals():

This method prints all animals currently in the zoo.
5. Add a method sell_animal(animal_sold):

This method checks if a specified animal exists on the animals list and if so, remove from it.
6. Add a method sort_animals():

This method sorts the animals alphabetically.
It also groups them by the first letter of their name.
The result should be a dictionary where:
Each key is a letter.
Each value is a list of animals that start with that letter.
Example output:

{
   'B': ['Baboon', 'Bear'],
   'C': ['Cat', 'Cougar'],
   'G': ['Giraffe'],
   'L': ['Lion'],
   'Z': ['Zebra']
}
7. Add a method get_groups():

This method prints the dict_animals animals as created by sort_animals().
Example output:

B: ['Baboon', 'Bear']
C: ['Cat', 'Cougar']
G: ['Giraffe']
...
"""

class Zoo():
    def __init__(self,zoo_name):

        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self,animal_sold):
        for animal in self.animals:
            if animal_sold in self.animals:
                self.animals.remove(animal_sold)

    # Sort animal
    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        dict_animals = {}
        
        # Loop into sorted animal
        # If the first letter is not in the dictionary, we put as key this first letter
        # And as value, we assign the animal with the append() function
        # The method returns the dictionnary created

        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in dict_animals:
                dict_animals[first_letter] = []
            dict_animals[first_letter].append(animal)
        return dict_animals

    def get_groups(self):
        groups = self.sort_animals()
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")


# Step 2: Create a Zoo instance
brooklyn_safari = Zoo("Brooklyn Safari")

# Step 3: Use the Zoo methods
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Babouin")
brooklyn_safari.get_animals()
print("-----")
brooklyn_safari.sell_animal("Bear")
print("-----")
brooklyn_safari.get_animals()
brooklyn_safari.sort_animals()
brooklyn_safari.get_animals()
brooklyn_safari.get_groups()