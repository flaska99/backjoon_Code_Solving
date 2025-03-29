## 연결요소 탐색 
import sys

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visted = [False] * (n+1)
count = 0

def dfs(num):
    global count
    if not visted[num]:
        visted[num] = True
        count += 1
        for target in graph[num]:
            dfs(target)

dfs(1)
print(count - 1) ## 자기 자신은 빼줌