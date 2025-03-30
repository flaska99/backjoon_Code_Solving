import sys
from collections import deque 

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[False]*m for _ in range(n)]
graph = [list(map(str, list(input().strip()))) for _ in range(n)]
end_x = end_y = 0
animal_que = deque()
water_que = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            animal_que.append((i, j))
        if graph[i][j] == 'D':
            end_x = i; end_y = j
        if graph[i][j] == '*':
            water_que.append((i,j))

t_x = [-1, 0, 1, 0]
t_y = [0, 1, 0, -1]
## 물먼저 저 방향으로 늘어나고 그 다음 
## 고슴도치 좌표가 늘어남..

time = 0

while animal_que:
    time+=1
    # 물 먼저 퍼뜨리기
    for _ in range(len(water_que)):
        x, y = water_que.popleft()
        for i in range(4):
            nx = x + t_x[i]
            ny = y + t_y[i]
            # 범위 안이고, 빈 칸이면
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.':
                graph[nx][ny] = '*'
                water_que.append((nx, ny))

# 그 다음 고슴도치 이동
    for _ in range(len(animal_que)):
        x, y = animal_que.popleft()
        for i in range(4):
            nx = x + t_x[i]
            ny = y + t_y[i]
            # 도착 지점
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'D':
                    print(time)
                    sys.exit()
                if graph[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    animal_que.append((nx, ny))

print('KAKTUS')