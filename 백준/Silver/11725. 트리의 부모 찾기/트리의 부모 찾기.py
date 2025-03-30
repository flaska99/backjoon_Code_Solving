import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input().strip())

graph = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for i in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# def bfs(start):
#     queue = deque([start])
#     while queue:
#         current = queue.popleft()

#         for neighbor in graph[current]:
#             if parent[neighbor] == 0:
#                 parent[neighbor] = current
#                 queue.append(neighbor)

# bfs(1)

def dfs(current, p):
    parent[current] = p

    for neighbor in graph[current]:
        if parent[neighbor] == 0:
            dfs(neighbor, current)

dfs(1, 0)
for i in range(2, n+1):
    print(parent[i])


