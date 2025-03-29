#n*m의 크기 노드의 개수는 n*m개
# 간선의 개수는 1의 개수
# 1이 있는 곳의 좌표를 큐에 넣음
# 순서대로 ? 탐색은 어떻게 ?
# (n, m) 에 도착할 수있는 이동해야하는 칸수 ! 
# 위, 아래, 오른쪽, 왼쪽을 탐색

from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, list(input().strip()))) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    que = deque()
    que.append((x,y))

    while que :
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                que.append((nx, ny))


    return maze[n-1][m-1]

print(bfs(0,0))

