sudokuBoard = []
print('When inputting the sudoku board, please enter the values in the row, separated by spaces.')
print('Note that empty squares should be entered as zero.')
print('An example row input might look like the following:')
print('1 2 0 7 4 0 5 9 3')
print()
for i in range(9):
    print(f'Please enter the values of row {i+1}.')
    inputRow = input().split()
    for i in range(len(inputRow)):
        inputRow[i] = int(inputRow[i])
    sudokuBoard.append(inputRow)


def solve(board):
    found = findEmptySpace(board)
    if not found:
        return True

    for i in range(1, 10):
        if validity(board, i, found):
            board[found[0]][found[1]] = i

            # continue along the current solution attempt, return True if it works
            if solve(board):
                return True

            # the backtracking point - if the solution attempt fails, this space goes back to zero and another
            # possible number will be tried in the for loop
            board[found[0]][found[1]] = 0


# check if a specific potential number is valid in a spot on the board
def validity(board, num, spot):
    # checking the row
    for i in range(len(board[0])):
        if spot[1] != i and board[spot[0]][i] == num:
            return False

    # checking the column
    for i in range(len(board[0])):
        if spot[0] != i and board[i][spot[1]] == num:
            return False

    # checking the "square" (3 by 3 sub-square in the board)
    ''' i use the // operator for this, which is "floor division". Take the x and y coordinates of the spot and floor 
        divide them by 3; meaning divide and then round down to the nearest integer. This allows me to take the 9x9 
        sudoku board and simplify it into a 3x3 grid of "squares", in which each square is another 3x3 grid, and check
        the squares as such. '''
    squareY = spot[0] // 3
    squareX = spot[1] // 3
    for i in range(squareY * 3, squareY * 3 + 3):
        for j in range(squareX * 3, squareX * 3 + 3):
            if (i, j) != spot and board[i][j] == num:
                return False

    return True


# find the first empty space in the board
def findEmptySpace(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # NOTE: this returns the coordinates as y, x

    return False


# print the board
def displayBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('-----------------------')
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')
            print(str(board[i][j]) + ' ', end='')
        print()


print('Unsolved Sudoku Board\n')
displayBoard(sudokuBoard)
print('\nSolved Sudoku Board\n')
solve(sudokuBoard)
displayBoard(sudokuBoard)
