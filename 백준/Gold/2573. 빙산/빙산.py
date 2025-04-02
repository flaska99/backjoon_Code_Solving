import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]

def bfs(x,y,visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q :
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m :
                if not visited[nx][ny] and graph[nx][ny] > 0:
                    visited[nx][ny] = True
                    q.append((nx,ny))

def count_icebergs():
    visited = [[False] * m for _ in range(n)]
    count = 0
    for i in range(n):
        for ii in range(m):
            if not visited[i][ii] and graph[i][ii] > 0 :
                bfs(i, ii, visited)
                count += 1
    
    return count

def melt():
    melt = [[0] * m for _ in range(n)]

    for i in range(n):
        for ii in range(m):
            if graph[i][ii] > 0:
                sea = 0

                for index in range(4):
                    nx =  i + dx[index]
                    ny = ii + dy[index]

                    if 0 <= nx < n and 0 <= ny < m:
                        if graph[nx][ny] == 0:
                            sea += 1
                melt[i][ii] = sea
    
    for I in range(n):
        for II in range(m):
            if graph[I][II] > 0:
                graph[I][II] = max(0, graph[I][II] - melt[I][II])

year = 0
while True:
    count = count_icebergs()

    if count == 0:
        print(0)
        break
    
    if count >= 2:
        print(year)
        break

    melt()
    year += 1

