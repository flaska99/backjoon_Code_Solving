import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

indegree = [0] * (n+1) # 진입차수
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    queue =deque()

    for i in range(1, n+1):
        # 진입차수가 0인 정점이라면
        if indegree[i] == 0:
            queue.append(i)
        
    while queue:
        current = queue.popleft()
        result.append(current)

        for i in graph[current]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    
    for i in result:
        print(i, end=' ')

topology_sort()