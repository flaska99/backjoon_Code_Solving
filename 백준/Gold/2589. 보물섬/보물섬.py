import sys
from collections import deque

input = sys.stdin.readline

col, row = map(int, input().split())

graph = [input().strip() for _ in range(col)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(start_x, start_y):
    visited = [[0]*row for _ in range(col)]
    que = deque()
    que.append((start_x, start_y))
    visited[start_x][start_y] = 1
    count = 0

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<= nx < col) and (0<= ny < row) and graph[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                count = max(count, visited[nx][ny])
                que.append((nx,ny))


    return count-1


max_count = 0

for i in range(col):
    for ii in range(row):
        if graph[i][ii] == 'L':
            max_count = max(bfs(i,ii), max_count)

print(max_count)
