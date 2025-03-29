import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)

def dfs(n) :
    visited[n] = True
    for next in graph[n]:
        if not visited[next]:
            visited[next] = True
            dfs(next)

count = 0
for i in range(1, len(visited)):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)
