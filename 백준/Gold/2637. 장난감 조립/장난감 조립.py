import sys
from collections import deque

## 위상정렬을 써야함..
## 위상정렬의 개념 ? 
## 진입차수를 생각해야함... 
## 이 문제에서 진입차수는 각 하위 부품을 얘기함 


input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
needs = [[0] * (n+1) for _ in range(n+1)]
indegree = [0] * (n+1)
que = []

## 그래프 생성 : 그래프는 단방향
for _ in range(m):
    x,y,z = map(int, input().split())
    graph[y].append((x,z))
    indegree[x] += 1


que = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        que.append(i)

while que:
    now = que.popleft()
    for next, count in graph[now]:
        if all(n == 0 for n in needs[now]):
            needs[next][now] += count
        
        else:
            for i in range(1, n+1):
                needs[next][i] += needs[now][i] * count
        
        indegree[next] -= 1

        if indegree[next] == 0:
            que.append(next)

for i in range(1, n):
    if needs[n][i] > 0:
        print(i, needs[n][i])