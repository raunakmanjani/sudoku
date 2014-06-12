# Sudoku Solver Project
# Developer- Raunak Manjani
import time
import MySQLdb

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
    #need it for debugging dont remove
'''def print_it(sudoku):
    for i in range(0,9):
        x=''
        for j in range(0,9):
            x=x+str(sudoku[i][j])+" "
        print x'''
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


def start(tree):
    sudoku = []
    a=tree
    z=[int(a[0])]
    for j in range(1,81):
        if j%9!=0:
            z.append(int(a[j]))

        else:
            sudoku.append(z)
            z=[int(a[j])]
            
    sudoku.append(z)
    solve(sudoku)
    strng=''
    for i in range(0,9):
        for j in range(0,9):
            strng=strng+str(sudoku[i][j])
    return strng
    

print "Initiating server"
tt = 1
while(tt==1):
    db = MySQLdb.connect(host="localhost",user="pydoku",passwd="su2048",db="sudoku")
    cur = db.cursor()
    print "begin"
    cur.execute("SELECT id,data FROM masty where status='0' order by id asc")
    for row in cur.fetchall():
        id1 = row[0]
        ss = row[1]
        print id1
        print ss
        if(ss!=""):
            out = start(ss)
            print out    
            yy = "UPDATE masty SET `status`='1', `ot`='%s' WHERE `id`=%s" % (out,id1)
            cur.execute(yy)
            db.commit()
            print "updated"
    cur.close()  
    db.close()
    time.sleep(1)  