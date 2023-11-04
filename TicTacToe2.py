board = ['-','-','-',
        '-','-','-',
        '-','-','-',]

cp = 'X'
winner = None
gameRunning = True

# game board
def printBoard(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('----------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('----------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print(f'Turn: {cp}')

# player input
def playerInput(board):
    inp = int(input('Enter number 1-9: '))
    if inp >= 1 and inp <= 9 and board[inp-1] == '-':
        board[inp-1] = cp
    else:
        gameRunning = False
        print('ERROR :)')
        

# win/tie 
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[1]
        return True
    elif board[3] == board[4] == board[5] and board[4] != '-':
        winner = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[8] != '-':
        winner = board[7]
        return True

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != '-':
        winner = board[3]
        return True
    elif board[1] == board[4] == board[7] and board[4] != '-':
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[5] != '-':
        winner = board[5]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[4] != '-':
        winner = board[4]
        return True
    elif board[2] == board[4] == board[6] and board[4] != '-':
        winner = board[4]
        return True
    
def checkTie(board):
    if '-' not in board:
        print('----------Tie----------')
        return True

def checkWin():
    if checkHorizontal(board) or checkDiagonal(board) or checkVertical(board):
        print(f'----------Winner: {winner}----------')
        return True

# switch player
def switchPlayer():
    global cp
    if cp == 'X':
        cp = 'O'
    else:
        cp = 'X'

# stop game
def checkStop():
    if checkWin() or checkTie(board):
        gameRunning = False

while gameRunning == True:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    checkStop()