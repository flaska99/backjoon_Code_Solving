import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

queue = deque([x])

while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
        if distance[neighbor] == -1:
            distance[neighbor] = distance[current] + 1
            queue.append(neighbor)

result = []

for i in range(1, n+1) :
    if distance[i] == k :
        result.append(i)

if result:
    result.sort()
    for city in result:
        print(city)

else:
    print(-1)



