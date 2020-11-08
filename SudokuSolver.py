board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve():
    empty=find_empty()
    if(empty!=None):
        x,y=empty
    else:
        return True
    for i in range(1,10):
        if isvalid(i,empty):
            board[x][y]=i
            if solve():
                return True
            board[x][y]=0
    return False
            
    
def isvalid(num,pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    y = pos[0]// 3
    x = pos[1]// 3
    for i in range(y*3, y*3 + 3):
        for j in range(x * 3, x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
    print()

def find_empty():
    for i in range (len(board)):
        for j in range (len(board[i])):
            if board[i][j]==0:
                return (i,j)
    return None

solve()
print_board(board)

