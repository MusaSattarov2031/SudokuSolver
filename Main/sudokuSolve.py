import numpy as np
#sudokuReader.py file will return an array with zeroes as empty numbers and other numbers. 
#Then solve function will solve sudoku and return a new array as result
def isValid(sudoku, row, col, num):
    if num in sudoku[row]:
        return False
    
    if num in sudoku[:, col]:
        return False
    
    start_row, start_col=3*(row//3), 3*(col//3)
    if num in sudoku[start_row:start_row+3, start_col:start_col+3]:
        return False
    
    return True

def solve(sudoku):
    empty_cell=np.argwhere(sudoku==0)
    #Initilizing empty cells

    if empty_cell.size==0:
        return sudoku
    # No empty cells, puzzle solved

    row, col=empty_cell[0]
    #Initilizing first empty cell

    for num in range (1, 10):
        if isValid(sudoku, row, col, num):
            sudoku[row, col]=num
            #Trying to put some value to this cell
            if solve(sudoku) is not None:
                return solve(sudoku)
            #Backtrack

            sudoku[row, col]=0

    return None

