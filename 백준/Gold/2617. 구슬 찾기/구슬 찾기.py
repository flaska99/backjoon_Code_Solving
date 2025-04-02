import sys
from collections import defaultdict, deque

def bfs(start, graph, n):
    visited = [False] * (n+1)
    queue = deque([start])
    visited[start] = True
    count = 0

    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                count += 1
    return count

input = sys.stdin.readline
n, m = map(int, input().split())

heavy_graph = defaultdict(list)
light_graph = defaultdict(list)

for _ in range(m):
    a,b = map(int, input().split())
    heavy_graph[a].append(b)
    light_graph[b].append(a)


threshold = n // 2
ans = 0


for i in range(1, n+1):
    heavier = bfs(i, heavy_graph, n)
    lighter = bfs(i, light_graph, n)
    
    if heavier > threshold or lighter > threshold:
        ans += 1

print(ans)