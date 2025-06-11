from collections import deque

def solution(n, wires):
    answer = n  # 최대값은 n이므로 초기값을 n으로 설정
    
    for num in range(len(wires)):
        graph = [[] for _ in range(n+1)]
        for i in range(len(wires)):
            if i == num:
                continue 
            a, b = wires[i]
            graph[a].append(b)
            graph[b].append(a)
        
        cnt = bfs(graph, n)
        diff = abs((n - cnt) - cnt)
        answer = min(answer, diff)
    
    return answer

def bfs(graph, n):
    visited = [False] * (n+1)
    que = deque()
    que.append(1)
    visited[1] = True
    count = 1
    
    while que:
        cur = que.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                que.append(next)
                count += 1
    return count
