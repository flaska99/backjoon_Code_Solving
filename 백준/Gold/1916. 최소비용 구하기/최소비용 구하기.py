import sys, heapq

input = sys.stdin.readline

INF = int(1e8)
n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    x, y, c = map(int, input().split())
    graph[x].append((y,c))

def bfs(start):
    bus = []
    heapq.heappush(bus, (0, start))
    distance[start] = 0

    while bus:
        c , now = heapq.heappop(bus)

        if c > distance[now]:
            continue

        for neighbor, cost in graph[now]:
            weight = c + cost
            if weight < distance[neighbor]:
                distance[neighbor] = weight
                heapq.heappush(bus, (weight, neighbor))

k, d = map(int, sys.stdin.readline().split())

bfs(k)
print(distance[d])