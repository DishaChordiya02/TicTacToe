import random

board=["-","-","-",
       "-","-","-",
       "-","-","-"]

gamerunning=True
Winner=None
currentplayer="X"

#game board
def printboard(board):
    print(board[0]+" | " +board[1]+" | " +board[2])
    print("---------")
    print(board[3] +" | " + board[4] +" | " + board[5])
    print("----------")
    print(board[6] +" | " + board[7] + " | " +board[8])

#take player input
def playerinput(board):
    inp=int(input("Enter tha value from 1-9:"))
    if inp>=1 and inp<=9 and board[inp-1]=="-":
        board[inp-1]=currentplayer

    else:
        print("Player is already on the spot")

#Check for win or tie

#check horizontal win
def checkhorizontal(board):
    global winner
    if board[0]== board[1]==board[2] and board[1]!="-":
        winner=board[0]
        return True

    if board[3]== board[4]==board[5] and board[3]!="-":
        winner=board[3]
        return True

    if board[6]== board[7]==board[8] and board[6]!="-":
        winner=board[6]
        return True

#check for vertical win
def checkvertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[3]
        return True

    if board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True

    if board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

#check for diagonal win
def checkdiagonal(board):
    global winner
    if board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[4]
        return True

def checkwin():
    if checkdiagonal(board) or checkhorizontal(board) or checkvertical(board):
        print(f"The winner is {winner}")

#check for tie
def checktie(board):
    global gamerunning
    if "-" not in board:
        printboard(board)
        print("It's a tie!!")
        gamerunning=False

#Switch player
def switchplayer():
    global currentplayer
    if currentplayer=="X":
        currentplayer="O"
    else:
        currentplayer="X"

def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()
while gamerunning:
    printboard(board)
    playerinput(board)
    checkwin()
    checktie(board)
    switchplayer()
    computer(board)
