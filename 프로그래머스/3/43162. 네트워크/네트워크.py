from collections import deque

def solution(n, computers):
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    count = 0
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i+1].append(j+1)
                
    for i in range(1, n+1):
        if visited[i] == 0:
            bfs(i, graph, visited)
            count += 1
    
    return count
        
                
def bfs(start, graph, visited): 
    que = deque()
    
    que.append((start))
    visited[start] = 1
    
    while que:
        current = que.popleft()
        
        for neighbor in graph[current]:
            if visited[neighbor] == 0:
                que.append(neighbor)
                visited[neighbor] = 1
                
    return visited
    
    
    
        