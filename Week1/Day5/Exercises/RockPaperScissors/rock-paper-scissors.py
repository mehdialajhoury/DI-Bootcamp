import game

"""rock-paper-scissors.py : create 3 functions
get_user_menu_choice() - this should display a simple menu, get the user’s choice (with data validation), and return the choice. No looping should occur here.
The possibles choices are : Play a new game or Show scores or Quit

print_results(results) – this should print the results of the games played. It should have a single parameter named results; which will be a dictionary of the results of the games played. It should display these results in a user-friendly way, and thank the user for playing.


Note: results should be in this form: {win: 2,loss: 4,draw: 3}. Bear in mind that this dictionary will need to be created and populated in some other part of our code, and passed in to the print_results function at the right time.

main() - the main function. It should take care of 3 things:
Displaying the menu repeatedly, until the user types in the value to exit the program: ‘x’ or ‘q’, whatever you decide. (Make use of the get_user_menu_choice function)

When the user chooses to play a game:
Create a new Game object (see below), and call its play() function, receiving the result of the game that is returned.
Remember the results of every game that is played.

When the user chooses to exit the program, call the print_results function in order to display a summary of all the games played.
"""
# User Menu : play a new game or quit (with printing result choice)
def get_user_menu_choice():
    user_choice = input("Menu\n(g) Play a new game\n(x) Show scores and exit")
    return user_choice

# Prints the final results when exiting the game
def print_results(results):

    print(f"Game Results :\nYou won {results["win"]} times\nYou lost {results["loss"]} times\nYou drew {results["draw"]} times")
    print("\n")
    print("Thank you for playing !")

# Main function : Looping while User doesn't quit the game
# Printing the game menu choice with the get_user_menu_choice() function
# Instanciation of the class Game()
# Launching the play() method and get results from it
# Updating the dictionnary (which is initialized at the start) with the total of the results : the value in incremented
def main():
    dict_results = {"win" : 0, "loss" :0, "draw" : 0}
    while(True):
        user_choice = get_user_menu_choice()
        if user_choice == "g":
            game1 = game.Game()
            result = game1.play()
            dict_results.update({result: dict_results.get(result, 0) + 1})
        elif user_choice == "x":
            print_results(dict_results)
            break

# Run the game !
main()