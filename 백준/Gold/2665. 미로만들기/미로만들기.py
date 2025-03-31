import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

def miRo_chotGi():
    visited = [[-1]*n for _ in range(n)]

    visited[0][0] = 0 # 시작점

    que = deque()
    que.append((0,0))
    # step = 0
    while que:
        x, y = que.popleft()

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        for i in range(4):
            nx = dx[i] + x; ny = dy[i] + y  # 방향설정

            if 0 <= nx < n and 0 <= ny < n:
                cost = visited[x][y]

                if board[nx][ny] == 1:
                    if visited[nx][ny] == -1 or visited[nx][ny] > cost:
                        visited[nx][ny] = cost
                        que.appendleft((nx, ny)) #흰방은 우선순위를 높게
                
                else:
                    if visited[nx][ny] == -1 or visited[nx][ny] > cost + 1:
                        visited[nx][ny] = cost + 1
                        que.append((nx,ny)) ## 검은방은 우선순위를 
                
        # print(f"\n[step {step}] visited 상태:")
        # for i in range(n):
        #     for j in range(n):
        #         v = visited[i][j]
        #         print("." if v == -1 else v, end=" ")
        #     print()
        # step += 1

    return visited[n-1][n-1]

print(miRo_chotGi())
