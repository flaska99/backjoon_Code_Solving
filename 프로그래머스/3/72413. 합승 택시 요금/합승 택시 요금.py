INF = float('inf')

def solution(n, s, a, b, fares):
    dist = [[INF] * (n+1) for _ in range(n+1)] 
    
    for i in range(1, n+1):
        dist[i][i] = 0    
    
    for u, v, cost in fares:
        dist[u][v] = cost
        dist[v][u] = cost
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    min_cost = INF
    for k in range(1, n+1):
        min_cost = min(min_cost, dist[s][k] + dist[k][a] + dist[k][b])
    
    return min_cost
    