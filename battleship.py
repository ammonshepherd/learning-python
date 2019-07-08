# Exercise 12.7 Create a program that is a simplified version of the game
# “Battleship.” The computer creates (in memory) a grid that is 4 cells wide
# and 3 cells high. The rows of the grid are numbered 1 to 3, and the columns
# of the grid are labeled A to D. The computer hides a battleship in three
# random cells in the grid. Each battleship occupies exactly one cell.
# Battleships are not allowed to touch each other horizontally or vertically.
# Make sure that the program places the battleships randomly, so not
# pre-configured.

# The computer asks the player to “shoot” at cells of the grid. The player does
# so by entering the column letter and row number of the cell which he wants to
# shoot at (e.g., "D3"). If the cell which the player shoots at contains
# nothing, the computer responds with “Miss!” If the cell contains a
# battleship, the computer responds with “You sunk my battleship!” and removes
# the battleship from the cell (i.e., a second shot at the same cell is a
# miss). As soon as the player hits the last battleship, the computer responds
# with displaying how many shots the player needed to shoot down all three
# battleships, and the program ends.

# To help with debugging the game, at the start the computer should display the
# grid with periods marking empty cells and Xs marking cells with battleships.
# Hint: If you have troubles with this exercise, start by using a board which
# has the bat- tleships already placed. Once the rest of the code works, add a
# function that places the battleships at random, at first without checking if
# they are touching one another. Once that works, add code that disallows
# battleships touching each other.

from random import random, randint, seed
from os import system, name
seed()

def clearTerminal():
    if name == "posix":
        _ = system("clear")
    else:
        _ = system("clr")

def generateBoard(rows, cols):
    the_board = []
    for r in range(rows):
        the_board.append([])
        for c in range(cols):
            the_board[r].append("-")
    with_ships = placeBattleships(the_board)
    return with_ships

def displayBoard(board):
    cols = len(board[0])
    rows = len(board)
    print(" ", end="") # The first line needs an extra space
    # Print out the columns header
    for a in range(cols):
        if a == cols - 1:
            print("   {}".format(chr(65+a)))
        else:
            print("   {}".format(chr(65+a)), end="")

    # display the top horizontal bar
    print('  _', end='')
    for x in range(cols * 4):
        if x == (cols * 4) - 1:
            print("_")
        else:
            print("_", end="")

    for n in range(len(board)):
        print("{} |".format(n + 1), end="") # print the row header
        for d in range(cols):
            # print the content of the cell, the last time with a hard return
            if d == cols - 1:
                #print(" {} |".format(board[n][d])) 
                print(" {} |".format(" ")) 
            else:
                #print(" {} |".format(board[n][d]), end="") 
                print(" {} |".format(" "), end="") 
        # Display the horizontal bars
        print('  _', end='')
        for x in range(cols * 4):
            if x == (cols * 4) - 1:
                print("_")
            else:
                print("_", end="")

# prompts for the cell
# returns a tuple with column converted to a number, A=0, B=1, C=2, etc.
# returns (column, row) since that is how it is asked for
# returns column and row as the index number
def guess(board):
    while True:
        guess = input("Enter a cell location (ex. D3, B2, A4): ")
        letter = guess[0].upper()
        number = int(guess[1])
        rows = len(board)
        cols = len(board[0])

        # if letter is  a string
        if isinstance(letter, str):
            # if letter between ASCII for A and however many columns there are
            if 65 > ord(letter) or ord(letter) > 64 + cols:
                print("Column not correct. Try again.")
                continue
        else:
                print("Column not correct. Try again.")
                continue

        # check the row
        if 1 > number or number > rows:
            print("Row not correct. Try again.")
            continue

        colIndex = ord(letter) - 65
        rowIndex = number - 1
        return (colIndex, rowIndex)
    
def isBattleship(guess, board):
    col = guess[0]
    row = guess[1]

    cell = board[row][col]
    if cell == '-':
        return False
    elif cell == 'x':
        return True
    else:
        return False

def updateBoard(guess, board):
    col = guess[0]
    row = guess[1]
    board[row][col] = "-"

def numBattleships(board):
    ships = 0
    for r in board:
        for c in r:
            if c == "x":
                ships += 1
    return ships

def placeBattleships(board):
    # must place ships randomly
    # number determined by how big the grid
    # ships can not touch each other on any side
    numRows = len(board)
    numCols = len(board[0])
    # number of ships equals the total number of cells divided by 4, just because
    numShips = (numRows * numCols) // 4 # use integer division to get a whole number

    # randomly place a ship 
    s = 1
    while s <= numShips:
        s += 1
        if s == 12: # stop with ten, anymore than that and it's just rediculous
            break
        randRowIndex = randint(0, numRows - 1)
        randColIndex = randint(0, numCols - 1)
        # if the cell already has an x, move on, but decrement the counter so
        # there will still be the right number of ships
        if board[randRowIndex][randColIndex] == "x":
            s -= 1
            continue

        # if cell above? does it have an x, if so decrement counter  and continue
        if  randRowIndex > 0 and board[randRowIndex - 1][randColIndex] == "x":
            s -= 1
            continue
        # if cell below? does it have an x, if so decrement counter  and continue
        if randRowIndex < numRows - 1 and board[randRowIndex + 1][randColIndex] == "x":
            s -= 1
            continue
        # if cell right? does it have an x, if so decrement counter  and continue
        if randColIndex < numCols - 1 and board[randRowIndex][randColIndex + 1] == "x":
            s -= 1
            continue
        # if cell left? does it have an x, if so decrement counter  and continue
        if randColIndex > 0 and board[randRowIndex][randColIndex - 1] == "x":
            s -= 1
            continue
        board[randRowIndex][randColIndex] = "x"
    return board


rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
# if they go crazy with the numbers, just limit to 10x10
if 0 > rows > 10:
    rows = 10
if  0 > columns > 10:
    columns = 10 

game_board = generateBoard(rows,columns)
guesses = 0
message = ''
while True:
    clearTerminal()
    ships = numBattleships(game_board)
    if ships > 0:
        print("Guesses: {} {}".format(guesses, message))
        print("There are {} ships left.".format(ships))
    else:
        print("You sunk all the battleships!")
        print("It took you {} guesses!".format(guesses))
        print("Game Over!")
        break
    displayBoard(game_board)
    my_guess = guess(game_board)
    guesses += 1
    if isBattleship(my_guess, game_board):
        message = ">> HIT! <<"
        updateBoard(my_guess, game_board)
    else:
        message = ">> MISS! Try again. <<"

# if __name__ == '__main__':
#     game_board = generateBoard(3,4)
#     displayBoard(game_board)

