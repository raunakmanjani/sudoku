# Sudoku Solver Project
# Developer- Raunak Manjani
import time
sud=[]

# basic functions to test
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
# manual method not to be used now
#    if(block%3==0):
 #       x=((block//3)-1)*3
  #  else:
  #      x=(block//3)*3
   # y=3*((block+2)%3)
    #c=x+3
#    d=y+3
 #   for i in range(x,c):
 #       for j in range(y,d):
  #          a.append(sudoku[i][j])
   # 
#    if number in a:
 #       return False
  #  else:
   #     return True
    start_row = (block / 3) * 3
    start_col = (block % 3) * 3
    for x in range(0,9):
        if(sudoku[start_row + (x / 3)][start_col + (x % 3)] == number):
            return False
    return True




# checks if the number can be inserted into the sudoku grid, uses 3 functions defined above

def is_possible_number(sudoku, row, col, number) :
    
    block=get_cell_block(row,col)
    if(is_possible_row(sudoku, row, number) and is_possible_column(sudoku, col, number) and is_possible_block(sudoku, block, number)):
        return True
    else:
        return False




#another method to solve, not needed, just written for kicks
'''    
def is_correct_row(sudoku, row) :
    
    a=sudoku[row]
    a.sort()
    b=False
    z=[1,2,3,4,5,6,7,8,9]
    if a==z:
        return True
    else:
        return False
        
def is_correct_column(sudoku, col) :
    
    z=[1,2,3,4,5,6,7,8,9]
    a=[]
    for i in range(0,9):
        a.append(sudoku[i][col])
    a.sort()
    if a==z:
        return True
    else:
        return False
    
def is_correct_block(sudoku, block) :
    
    a=[]
    z=[1,2,3,4,5,6,7,8,9]
    start_row = (block / 3) * 3
    start_col = (block % 3) * 3
    for x in range(0,9):
        a.append(sudoku[start_row + (x / 3)][start_col + (x % 3)])
    a.sort()
    if a==z:
        return True
    else:
        return False        
    
    
    
def is_solved(sudoku) :
    for x in range(0, 9):
          if not (is_correct_row(sudoku, x) and is_correct_column(sudoku, x) and is_correct_block(sudoku, x)):
            return False
    return True
'''



# prints the sudoku in a 9x9 format
def print_it(sudoku):
    for i in range(0,9):
        x=''
        for j in range(0,9):
            x=x+str(sudoku[i][j])+" "
        print x


#finds empty boxes in the sudoku, if there are no empty boxes it returns -1        
def findzero(sudoku):
    for i in range (0,9):
        for j in range(0,9):
            if sudoku[i][j]==0:
                return i,j
    return -1,-1





#Main sudoku solving function
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
        




# need to finish this method, another way to solve it, will try later but you can ignore it 

'''def solve(sudoku):
    a=[1,2,3,4,5,6,7,8,9]
    
    for i in range(0,9):
        for j in range(0,9):
            if (sudoku[i][j])>0:
                continue
            else:
                for k in range (0,9):
                    if is_possible_number(sudoku, i, j, a[k]):
                        sudoku[i][j]=a[k]
                        break'''





    
                        
# 2 methods to check if its solved correctly

'''def check(sudoku):
    for i in range(0,9):
        for j in range(0,9):
            a=sudoku[i][j]
            sudoku[i][j]=0
            if is_possible_number(sudoku,i,j,a):
                sudoku[i][j]=a
                continue
            else:
                print i,j
                return False
    return True

def check2(sudoku):
    s=0
    for i in range(0,9):
        for j in range(0,9):
            
            s+=sudoku[i][j]
        print s'''
    
                                  


sudoku= [[ 0, 6, 0,   0, 2, 0,   0, 0, 0 ],[ 9, 0, 0, 0, 0, 8, 0, 0, 0 ],[ 2, 0,4,   0, 9, 0,   0, 6, 0 ],[ 0, 0, 0,   0, 0, 0,   1, 3, 0 ],[ 3, 0, 0,   0, 0, 0,   0, 0, 2 ],[ 0, 0, 8,   0, 7, 4,   5, 0, 0 ],[ 0, 0, 3,   5, 0, 0, 6,0,0 ],[ 0, 8, 0,   0, 0, 0,   0, 0, 4 ],[ 0, 0, 5,   0, 0, 0,8, 0, 0 ] ]
print_it(sudoku)
print ''
solve(sudoku)
print_it(sudoku)
'''
print check(sudoku)
print is_solved(sudoku)
#print check2(sudoku)'''
