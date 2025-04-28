import sys, heapq

input = sys.stdin.readline

def dijkstra(n, graph):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    INF = int(1e9)
    dist = [[INF]*n for _ in range(n)]
    dist[0][0] = graph[0][0]

    que = []
    heapq.heappush(que, (graph[0][0], 0, 0))

    while que:
        cost, x, y = heapq.heappop(que)

        if x == n-1 and y == n-1:
            return cost

        if dist[x][y] < cost:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                next_cost = cost + graph[nx][ny]
                if next_cost < dist[nx][ny]:
                    dist[nx][ny] = next_cost
                    heapq.heappush(que, (next_cost, nx, ny))

count = 1

while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    answer = dijkstra(n, graph)
    print(f"Problem {count}: {answer}")
    count += 1
