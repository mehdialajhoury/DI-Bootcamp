"""Instructions

The game is played on a grid that’s 3 squares by 3 squares.
Players take turns putting their marks (O or X) in empty squares.
The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.


Hint

To do this project, you basically need to create four functions:

display_board() – To display the Tic Tac Toe board (GUI).
player_input(player) – To get the position from the player.
check_win() – To check whether there is a winner or not.
play() – The main function, which calls all the functions created above.
Note: The 4 functions above are just an example. You can implement many more helper functions or choose a completely different appoach if you want."""


def display_board():
        
    matrix = [[" "," " ," " ], 
    [" "," " ," " ],
    [" "," " ," " ]]

    player = "X"
        
    while(True):

        if player == "X":
            player = "O"
        else:
            player ="X"

        print("Welcome to TIC TAC TOE!")
        print("*******************")
        print(f"*  {matrix[2][0]}   | {matrix[2][1]}  |  {matrix[2][2]}  *")
        print("*------|----|-----*")
        print(f"*  {matrix[1][0]}   | {matrix[1][1]}  |  {matrix[1][2]}  *")
        print("*------|----|-----*")
        print(f"*  {matrix[0][0]}   | {matrix[0][1]}  |  {matrix[0][2]}  *")
        print("*******************")
        
        print(f"Player {player} turn...")

        
        row_input = int(input("Enter row"))
        column_input = int(input("Enter column"))

        print(f"row chosen {row_input}")
        print(f"row chosen {column_input}")
        
        matrix[row_input-1][column_input-1] = player
        print(matrix)
        if check_win(matrix) is True:
            print(f"Player {player} won !")
            break

def check_win(matrix):
   
    #Check rows
    for row in matrix:
        if row[0] == row[1] == row[2] != " ":
            return True 
        
    # Check cols   
    for col in range(3):
        if matrix[0][col] == matrix[1][col] == matrix[2][col] != " ":
            return True

    # Check diag
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != " ":
        return True
    if matrix[0][2] == matrix[1][1] == matrix[2][0] != " ":
        return True

    # If no wins
    return None
    
player = "X"

display_board()