import random

"""game.py – this file/module should contain a class called Game. It should have 4 methods:
get_user_item(self) – Ask the user to select an item (rock/paper/scissors). Keep asking until the user has selected one of the items – use data validation and looping. Return the item at the end of the function.

get_computer_item(self) – Select rock/paper/scissors at random for the computer. Return the item at the end of the function. Use python’s random.choice() function (read about it online).

get_game_result(self, user_item, computer_item) – Determine the result of the game.
Parameters:
user_item – the user’s chosen item (rock/paper/scissors)
computer_item – the computer’s chosen (random) item (rock/paper/scissors)
Return either win, draw, or loss. Where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.

play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
Get the user’s item (rock/paper/scissors) and remember it

Get a random item for the computer (rock/paper/scissors) and remember it

Determine the results of the game by comparing the user’s item and the computer’s item
Print the output of the game; something like this: “You selected rock. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”

Return the results of the game as a string: win;draw;loss;, where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.
"""

class Game():

    def __init__(self):
        self.items = ["rock","paper","scissors"]

    # User menu for choosing between rock, paper and scissors
    # Return the item in the list attribute "items"
    def get_user_item(self):
        while(True):
            item_input = input("Please select (r)ock (p)aper or (s)cissors")
            if item_input == "r":
                return self.items[0]
            elif item_input =="p":
                return self.items[1]
            elif item_input == "s":
                return self.items[2]
    
    # Using method choice from random module to choose between elements in the attribute items
    # Return only 1 item randomly : rock, paper or scissors
    def get_computer_item(self):
        return random.choice(self.items)
    
    # Method in which all the possibilities are listed in if statements
    # We pass through the method the user item (rock, paper, scissorcs) and the computer item (same)
    # It returns the result of the confrontation : "draw", "loss" or "win"
    def get_game_result(self, user_item, computer_item):

        if user_item == computer_item:
            return "draw"
        elif user_item == "rock" and computer_item == "paper":
            return "loss"
        elif user_item == "rock" and computer_item == "scissors":
            return "win"
        elif user_item == "paper" and computer_item == "rock":
            return "win"
        elif user_item == "paper" and computer_item == "scissors":
            return "loss"
        elif user_item == "scissors" and computer_item == "rock":
            return "loss"
        elif user_item == "scissors" and computer_item == "paper":
            return "win"
        
    # Launch the confrontation between user and computer
    # Return the game result : "win", "loss" or "draw"
    def play(self):
        self.user_item = self.get_user_item()
        self.computer_item = self.get_computer_item()
        game_result = str(self.get_game_result(self.user_item,self.computer_item))
        print(f"You selected : {self.user_item}. The computer selected : {self.computer_item}. Result : {game_result}")
        
        return game_result