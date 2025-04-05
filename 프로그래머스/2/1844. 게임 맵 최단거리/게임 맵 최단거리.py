from collections import deque

def bfs(x, y, n, m, map):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    que = deque()
    
    que.append((x,y))
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
        
            if 0<= nx < n and 0<= ny < m and map[nx][ny] == 1:
                map[nx][ny] += map[x][y]
                que.append((nx,ny))
            
            if nx == n-1 and ny == m-1:
                return map[nx][ny]
    return -1
    
def find(map):
    n = len(map)
    m = len(map[0])
    
    return n,m

def solution(maps):
    answer = 0
    n, m = find(maps)
    
    return bfs(0,0,n,m,maps)
    
    
