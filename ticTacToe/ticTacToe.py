#! python 3
# tic tac toe board
theBoard = {'top-L':' ', 'top-M':' ', 'top-R':' ',
            'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
            'low-L':' ', 'low-M':' ', 'low-R':' '}
def printBoard(board):
    printBoard(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    printBoard(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    printBoard(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'x'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'x':
        turn = '0'
    else:
        turn = 'x'
printBoard(theBoard)