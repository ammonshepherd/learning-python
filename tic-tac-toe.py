board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def displayBoard(board):
    print("   1   2   3")
    for x in range(0, 3):
        print('{}  {} | {} | {}'.format(chr(x+65), board[x][0], board[x][1], board[x][2]))
        if x < 2:
            print('  ____________')

def getRowCol():
    while True:
        row = input("Enter the row (A, B, C): ")
        if row == 'A':
            row = 0
            break
        elif row == 'B':
            row = 1
            break
        elif row == 'C':
            row = 2
            break
        else:
            continue

    while True:
        col = input("Enter the column (1, 2, 3): ")
        if col == '1':
            col = 0
            break
        if col == '2':
            col = 1
            break
        if col == '3':
            col = 2
            break
        else:
            continue
    return row, col

def isCellEmpty(row, col, board):
    if board[row][col] == ' ':
        return True
    else:
        return False

def checkWinner(board):
    # all the options to win
    winningOptions = [
        [ [0,0], [0,1], [0,2] ], 
        [ [1,0], [1,1], [1,2] ], 
        [ [2,0], [2,1], [2,2] ], 
        [ [0,0], [1,1], [2,2] ], 
        [ [0,0], [1,0], [2,0] ], 
        [ [0,1], [1,1], [2,1] ], 
        [ [0,2], [1,2], [2,2] ],
        [ [0,2], [1,1], [2,0] ]
    ]

    for option in winningOptions:
        row1 = option[0][0]
        col1 = option[0][1]

        row2 = option[1][0]
        col2 = option[1][1]

        row3 = option[2][0]
        col3 = option[2][1]

        if (board[row1][col1] == 'x' and board[row2][col2] == 'x' and board[row3][col3] == 'x') or (board[row1][col1] == 'o' and board[row2][col2] == 'o' and board[row3][col3] == 'o'):
            return True
        else:
            continue

            
displayBoard(board)
player1 = input("Player 1, enter your name: ")
player2 = input("Player 2, enter your name: ")
mark = 'x'
turnCount = 1
while True:
    print()
    if mark == 'x':
        print("{}, it is your turn.".format(player1))
        isTurn = player1
    else:
        print("{}, it is your turn.".format(player2))
        isTurn = player2
    row, col = getRowCol()
    if isCellEmpty(row, col, board) == False:
        print()
        print("Cell is occupied. Try again")
        continue

    board[row][col] = mark
    displayBoard(board)
    if turnCount > 4:
        if checkWinner(board):
            print()
            print('Congratulations {}, you won!!'.format(isTurn))
            break
       
        else:
            if turnCount == 9:
                print()
                print("Cat's got the game!")
                break
        
    if mark == 'x':
        mark = 'o'
    else:
        mark = 'x'

    turnCount += 1