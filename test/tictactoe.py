
def insertLetter(board,letter, pos):
    board[pos] = letter
    return board


def spaceIsFree(board,pos):
    return board[pos] == ' '


def printBoard(board):
    str='Board \n'
    str+=' ' + board[1] + ' | ' + board[2] + ' | ' + board[3]
    str+='\n'
    str+='-----------'
    str+='\n'
    str+=' ' + board[4] + ' | ' + board[5] + ' | ' + board[6]
    str += '\n'
    str+='-----------'
    str += '\n'
    str+=' ' + board[7] + ' | ' + board[8] + ' | ' + board[9]
    return str


def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
                bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (
                       bo[2] == le and bo[5] == le and bo[8] == le) or (
                       bo[3] == le and bo[6] == le and bo[9] == le) or (
                       bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)


def playerMove(board,noo):
    run = True
    while run:
        # move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            noo = int(noo)
            if noo > 0 and noo < 10:
                if spaceIsFree(board,noo):
                    run = False
                    board=insertLetter(board,'X', noo)
                    return board,"Alright! Let's look at the board, shall we?"
                else:
                    return board,"Oops...This space is already occupied! Try again"
            else:
                return board,'I need a number between 1 and 9!'
        except:
            return board,'I need a number!'


def compMove(board):
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return board,move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return board,move

    if 5 in possibleMoves:
        move = 5
        return board,move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return board,move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
