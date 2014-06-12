# Sudoku Solver Project
# Developer- Raunak Manjani
def get_cell_block(row,col) :
    block_row = row / 3
    block_col = col / 3
    block = block_row*3 + block_col
    return block
def is_possible_row(sudoku, row, number):    
    if(number in sudoku[row]):
        return False
    else:
        return True
def is_possible_column(sudoku, col, number) :
    a=[]
    for i in range(0,9):
        a.append(sudoku[i][col])        
    if(number in a):
        return False
    else:
		return True
def is_possible_block(sudoku, block, number):
    a=[]
    start_row = (block / 3) * 3
    start_col = (block % 3) * 3
    for x in range(0,9):
        if(sudoku[start_row + (x / 3)][start_col + (x % 3)] == number):
            return False
    return True		
def is_possible_number(sudoku, row, col, number) :
    block=get_cell_block(row,col)
    if(is_possible_row(sudoku, row, number) and is_possible_column(sudoku, col, number) and is_possible_block(sudoku, block, number)):
        return True
    else:
        return False
def print_it(sudoku):
    for i in range(0,9):
        x=''
        for j in range(0,9):
            x=x+str(sudoku[i][j])+" "
        print x
def findzero(sudoku):
    for i in range (0,9):
        for j in range(0,9):
            if sudoku[i][j]==0:
                return i,j
    return -1,-1
def solve(sudoku):    
    i,j=findzero(sudoku)    
    if i==-1 and j==-1:
        return True
    for k in range (1,10):
        if is_possible_number(sudoku, i, j, k):
            sudoku[i][j]=k
        
            if(solve(sudoku)):
                return True
        
            sudoku[i][j]=0
    return False
sudoku= [[ 0, 6, 0,   0, 2, 0,   0, 0, 0 ],[ 9, 0, 0, 0, 0, 8, 0, 0, 0 ],[ 2, 0,4,   0, 9, 0,   0, 6, 0 ],[ 0, 0, 0,   0, 0, 0,   1, 3, 0 ],[ 3, 0, 0,   0, 0, 0,   0, 0, 2 ],[ 0, 0, 8,   0, 7, 4,   5, 0, 0 ],[ 0, 0, 3,   5, 0, 0, 6,0,0 ],[ 0, 8, 0,   0, 0, 0,   0, 0, 4 ],[ 0, 0, 5,   0, 0, 0,8, 0, 0 ] ]
print_it(sudoku)
print ''
solve(sudoku)
print_it(sudoku)