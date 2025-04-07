n = int(input())
m = int(input())
inf = 987_654_321
graph = [[inf] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] == inf and graph[j][i] == inf:
            count += 1
    print(count - 1)