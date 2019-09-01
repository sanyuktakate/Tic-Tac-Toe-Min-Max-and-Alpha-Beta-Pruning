'''
Name: Sanyukta Sanjay Kate
Algorithm Reference: Artificial Intelligence a modern approach and Geek for Geeks.

This is the program to play the Tic Tac Toe game using the Min Max Algorithm and Alpha Beta pruning
'''

#count is global variable, used for counting the number of nodes/states generated during min max and prunning
count=0

'''
InitializeBoard() is used for initially initialzing the board with null string
'''
def InitializeBoard(board):

    for i in range(0,3):
        row_board = []
        for j in range(0,3):
            row_board.append('null')
        board.append(row_board)
    return board

'''
startGame() is used for loading or starting the tic tac toe game which calls the minmax funxtion and the
alpha beta prunning
'''

def startGame(board):
    '''
    :param board: This is the board which shows the current state of the tic tac toe game
    :return: optimal row and column values for min max and alpha beta prunning
    '''

    global count

    #initially optimal_value and alphaBeta_value is -infinity
    optimal_value = -float('inf')
    alphaBeta_value = -float('inf')
    print()

    #for every board state (ie, board[row][column]) different tree is generated by calling the min max ad alpha beta pruning
    for row in range (0,3):
        for column in range(0,3):
            #make opponent's move on the board only if that particular position is empty
            if board[row][column] == 'null':

                board[row][column] = 'O'

                #Calculate the evaluation function for this move
                count = 1
                optimal_score = minmax(board, 0) #0 is going to be minimizer
                board[row][column] = 'null'
                #print()
                print("Number of Nodes generated in MIN MAX:", count)
                count = 0

                if optimal_score >= optimal_value:
                    optimal_value = optimal_score
                    optimal_row = row
                    optimal_column = column

                #----Alpha Beta----#
                board[row][column] = 'O'

                #calculate the evaluation function for this move
                count = 1
                alphaBetaScore = alphaBeta(board, 0, -float('inf'), float('inf'))
                board[row][column] = 'null'

                print("Number of Nodes generated in ALPHA BETA PRUNING:", count)
                print()
                count = 0

                if alphaBetaScore >= alphaBeta_value:
                    alphaBeta_value = alphaBetaScore
                    alphaBetaRow = row
                    alphaBetaColumn = column

    return optimal_row, optimal_column, alphaBetaRow, alphaBetaColumn

'''
alphaBeta() function gives the optimal coordinates after player's every move which is found by prunning some of
the branches. Few states are not generated but still give the same answer as the min max algorithm.
'''

def alphaBeta(board, player, alpha, beta):
    '''
    board shows the current state of the board.
    player is either 1 or 0. Where, 1 represents the 'X' (which is us-player), whereas the 0 represents the 'O' (opponent)
    '''
    global count

    #checkIfWinner() checks if player or the computer has won or not.
    winner = checkIfWinner(board)

    #if the winner is opponent, then rerurn 1. As one is the maximizer, we return the value as 1
    if winner == 'O':
        return 1
    #If the winner is the player, then return -1 as the value, as we are trying to reduce the chances of the maximizer
    #to win
    if winner == 'X':
        return -1

    #IsBoardFull() checks if the board is full with moves or not.
    if IsBoardFull(board) == False:
        return 0

    #start with the min max flipping depeding upon the player's state, which is 1 or 0
    if player == 1:  # maximizer is computer
        #When maximizer is playing kepp the maxVal as -infinity
        maxVal = -float('inf')

        #Create nodes/states depending upon the posiiton of the maximizer.
        for row in range(0, 3):
            for column in range(0, 3):
                if board[row][column] == 'null':
                    board[row][column] = 'O'
                    count+=1
                    maxVal = max(maxVal, alphaBeta(board, 0, alpha, beta))
                    board[row][column] = 'null'
                    #check if the value generated from the left side of the tree is greater than the beta value
                    #if yes, then return the maxValue
                    if maxVal >= beta:
                        return maxVal
                    #find the new alpha value
                    alpha = max(alpha, maxVal)
        return maxVal
    else:  #minimizer
        #when minimizer is playing, the minVal is infinity
        minVal = float('inf')

        #Calculate the value at minimizer using alpha beta pruning
        for row in range(0, 3):
            for column in range(0, 3):
                if board[row][column] == 'null':
                    board[row][column] = 'X'
                    #count calculates the number of nodes generated
                    count+=1
                    minVal = min(minVal, alphaBeta(board, 1, alpha, beta))
                    board[row][column] = 'null'

                    #if minVal is less than alpha then, return minVal
                    if minVal<=alpha:
                        return minVal
                    #update the beta value
                    beta = min(beta,minVal)
        return minVal

'''
CheckIfWinner() looks if there is any winner in the board by checking the rows and the columns and the diagonals too.
'''
def checkIfWinner(board):
    '''
    :param board: The board shows the current state of the board
    :return: returns eith 'X' or 'O' or 'null
    '
    '''
    #Calling the functions which check winner in rows, columns and diagonals
    val1 = checkRows(board)
    val2 = checkColumns(board)
    val3 = checkDiagonals(board)

    #return the values got
    if val1!='null':
        return val1
    if val2!='null':
        return val2
    if val3!='null':
        return val3

    #If none of the conditions satisfy then return 'null'
    return 'null'

def checkRows(board):
    '''
    :param board: shows the current state of the board
    :return: returns 'X' or 'O' or 'null'
    '''

    #checking the rows for winner
    row=0
    while row<3:
        if board[row][0]==board[row][1] and board[row][1] == board[row][2]:
            if board[row][0]=='X':
                return 'X'
            elif board[row][0] == 'O':
                return 'O'
        row+=1

    return 'null'

'''
checkColumns() checks the columns of the board for the winner.
'''
def checkColumns(board):
    '''

    :param board: gives the current state of the game
    :return: 'X' or 'O' or 'null'
    '''
    #checking columns for winner

    column = 0
    while column<3:
        if board[0][column]==board[1][column] and board[1][column]==board[2][column]:
            if board[0][column]=='X':
                return 'X'
            elif board[0][column]=='O':
                return 'O'
        column+=1
    return 'null'

'''
checkDiagonals() for the winner in diagonals
'''
def checkDiagonals(board):
    '''

    :param board: shows the current state of the game
    :return: 'X' or 'O' or 'null'
    '''
    #checking diagonals

    #left diagonal
    if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        if board[0][0] == 'X':
            return 'X'
        elif board[0][0] == 'O':
            return 'O'

    #right diagonal
    if board[0][2]==board[1][1] and board[1][1]==board[2][0]:
        if board[0][2]=='X':
            return 'X'
        elif board[0][2]=='O':
            return 'O'
    return 'null'

'''
IsBoardFull() checks if the entire board is filled with the players moves or not
'''
def IsBoardFull(board):
    '''

    :param board: shows the current state of the game
    :return: True or False
    '''
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j]=='null':
                return True
    return False

'''
minmax() is the function which generates different state depending upon the player's move. Gives the optimal score.
'''
def minmax(board, player):
    '''

    :param board: shows the current state of the game
    :param player: shows which player is playing
    :return: optimal score
    '''

    global count

    #check for winner
    winner = checkIfWinner(board)
    if winner == 'O':
        return 1
    if winner == 'X':
        return -1

    #check if board is filled with moves or not
    if IsBoardFull(board)==False:
        return 0

    if player==1: #maximizer is computer
        maxVal= -float('inf')

        for i in range(0,3):
            for j in range(0,3):
                if(board[i][j]=='null'):
                    #count the number of nodes/states generated
                    count+=1
                    board[i][j] = 'O'
                    maxVal = max(maxVal, minmax(board, 0))
                    #remove the move done
                    board[i][j] = 'null'
        #return optimal score
        return maxVal
    else: #minimizer
        minVal = float('inf')

        for i in range(0,3):
            for j in range(0,3):
                if board[i][j]=='null':
                    #count calculates the number of nodes generated
                    count+=1
                    board[i][j] = 'X'
                    minVal = min(minVal, minmax(board, 1))
                    #remove the move done
                    board[i][j] = 'null'
        #return the minimum score
        return minVal

'''
displayBoard(), displays the current state of the board
'''
def displayBoard(board):
    print("\n---BOARD---\n")
    for i in range(0,3):
        print(board[i])

'''
main() is used for calling the function which initializes the board and also, controls the game or the actual number
of moves made on the board.
'''
def main():
    board = InitializeBoard(board=[])

    #flag determines whose turn it is
    flag = True #True is players turn
    counter = 9
    IsDraw = True

    while counter>0:
        if flag: #players turn to play
            print("Player, Enter your move:")
            row = int(input())
            column = int(input())
            board[row][column] = 'X'
            counter = counter-1
            flag = False
        else:
            print('Opponent Plays')
            optimal_row, optimal_column, alphabetaRow, alphabetaColumn = startGame(board)
            print("The optimal coordinates for Min Max is:", optimal_row, optimal_column)
            board[optimal_row][optimal_column]='O'
            print("The optimal coordinates for aplha beta pruning is:", alphabetaRow, alphabetaColumn)
            displayBoard(board)
            print()

            #check if winner is found. In this case, winner shd always be the opponent which is the computer
            winnerIs = checkIfWinner(board)
            if winnerIs == 'O':
                IsDraw = False
                print()
                print("Opponent is the Winner!!!")
                break

            counter = counter-1
            flag = True

    if IsDraw==True:
        print("The match is a DRAW!")
if __name__ == "__main__":
    main()
