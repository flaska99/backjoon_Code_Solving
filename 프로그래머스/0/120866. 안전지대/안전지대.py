
def solution(board):
    n = len(board)
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                bfs(i,j,board)
                print(board)
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                count += 1
    
    return count

def bfs(x, y, board):
    
    dx = [-1,1,0,0,-1,1,-1,1]
    dy = [ 0,0,-1,1,-1,1,1,-1]
    
    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0<= nx < len(board) and 0<= ny < len(board) :
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                            

        