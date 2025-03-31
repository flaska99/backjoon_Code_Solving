import sys
from collections import deque
input = sys.stdin.readline

m, n, g = map(int, input().split())

graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(g)]
que = deque()



## 전체요소
total_tomato = 0 
## 토마토 없는 요소 갯수
not_tomato = 0
## 토마토 익은거 개수
is_tomato = 0

## 익은 토마토 좌표 세야함...
for i in range(g):
    for ii in range(n):
        for iii in range(m):
            if graph[i][ii][iii] == 1:
                que.append((i,ii,iii))
                is_tomato += 1
            elif graph[i][ii][iii] == -1:
                not_tomato += 1
            total_tomato += 1

## 다 익어있으면 걍 끝내버림
if total_tomato - not_tomato == len(que):
    print(0)
    sys.exit()

# total_tomato = sum(len(layer) * len(layer[0]) for layer in graph) ## 전체 요소 세기

## 아닐경우...

## 위, 아래, 왼쪽, 오른쪽, 앞, 뒤...
dx = [0,0,0,0,-1,1]##행
dy = [0,0,-1,1,0,0]##열
dz = [-1,1,0,0,0,0]##층..

time = -1
while que:
    for _ in range(len(que)):  # 현재 시점에서 익을 토마토들
        z, x, y = que.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nz < g and 0 <= nx < n and 0 <= ny < m:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = 1
                    is_tomato += 1
                    que.append((nz, nx, ny))
    time += 1  # 그룹(한 층) 처리 후 하루 증가

if not_tomato + is_tomato == total_tomato: print(time)
else: print(-1)