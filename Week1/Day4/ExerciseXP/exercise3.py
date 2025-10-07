from exercise1to2 import Dog
import random

"""Step 1: Import the Dog Class

In a new Python file, import the Dog class from the previous exercise.


Step 2: Create the PetDog Class

Create a class called PetDog that inherits from the Dog class.
Add a trained attribute to the __init__ method, with a default value of False.
trained means that the dog is trained to do some tricks.
Implement a train() method that prints the output of bark() and sets trained to True.
Implement a play(*args) method that prints “ all play together”.
*args on this method is a list of dog instances.
Implement a do_a_trick() method that prints a random trick if trained is True.
Use this list for the ramdom tricks:
tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
Choose a rendom index from it each time the method is called.


Step 3: Test PetDog Methods

Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() methods.


Example:

# In a new file
# import the Dog class

class PetDog(Dog):
    def __init__(self, name, age, weight): <mark> no need to put the details in the function, you are giving the solution</mark>
        super().__init__(name, age, weight)
        self.trained = False

    def train(self): <mark> no need to put the details in the function, you are giving the solution</mark>
        print(self.bark())
        self.trained = True

    def play(self, *args):
        # ... code to print play message ...

    def do_a_trick(self): <mark> no need to put the details in the function, you are giving the solution</mark>
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")

# Test PetDog methods
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()
"""

class PetDog(Dog):
    def __init__(self,name,age,weight,trained=False):
        self.name = name
        self.age = age
        self.weight = weight
        self.trained = trained

    def train(self):
        self.trained = True
        return self.bark()
    
    def play(self,*args):
        dogs_list_string = ""
        for dog in args:
            if dogs_list_string != "":
                dogs_list_string = dogs_list_string + ", " + dog.name
            else:
                dogs_list_string = dog.name
        print(f"{dogs_list_string} : all play together")

    def do_a_trick(self):
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        if self.trained is True:
            print(f"{self.name} {random.choice(tricks)}")
    
# Test Program

dog1 = PetDog("Bingo",15,13)
dog2 = PetDog("Shana",3,30)
dog3 = PetDog("Aspro",1,25)
print(dog1.train())
dog1.do_a_trick()
dog1.play(dog1,dog2,dog3)