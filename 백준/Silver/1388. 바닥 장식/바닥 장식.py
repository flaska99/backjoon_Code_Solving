import sys
sys.setrecursionlimit(10000)  # DFS 사용 시 깊이 제한 해제
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def dfs(x, y):
    visited[x][y] = True
    if graph[x][y] == '-':
        ny = y + 1
        if ny < m and graph[x][ny] == '-' and not visited[x][ny]:
            dfs(x, ny)
    elif graph[x][y] == '|':
        nx = x + 1
        if nx < n and graph[nx][y] == '|' and not visited[nx][y]:
            dfs(nx, y)

count = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j)
            count += 1

print(count)
