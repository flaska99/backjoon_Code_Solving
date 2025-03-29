import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

#dfs
visited_dfs = [False] * (n + 1)
def dfs(v):
    visited_dfs[v] = True
    print(v, end = ' ')
    for next in graph[v]:
        if not visited_dfs[next]:
            dfs(next)

#bfs
visited_bfs = [False] * (n+1)
def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True
    while queue:
        curr = queue.popleft()
        print(curr, end=' ')
        for next in graph[curr]:
            if not visited_bfs[next]:
                visited_bfs[next] = True
                queue.append(next)

dfs(v)
print()
bfs(v)