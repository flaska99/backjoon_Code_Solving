## 
import sys
from collections import deque

##일단 dfs로 방문을 하고 다음 노드가 0이라면 
## 재귀를 태움 이떄 이웃노드가 1이라면 count+=1 더이상의 재귀 안탐
## visted테이블을 통해 복수방문 관리

input = sys.stdin.readline

n = int(input()) ## n은 정점의 개수, n-1은 간선의 개수

view_recive = list(map(int, input().strip())) # n번쨰 실내 실외 정보 저장

## 편의를 위해 view테이블 재생성
## 편의를 위해 index n으로 늘려 저장
view = deque(view_recive)
view.appendleft(0)


visted = [0 for _ in range(n+1)]  ## 실내 실외 여부
graph = [[] for _ in range(n+1)] ## 간선 그래프

for _ in range(n-1):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

count = 0
def dfs(start):
    global count
    current = start
    visted[current] = 1
    for neightbor in graph[current]:
        if visted[neightbor] == 0 and view[neightbor] == 1:
            count+=1
        elif visted[neightbor] == 0 and view[neightbor] == 0:
            dfs(neightbor)
    
for i in range(1, n+1):
    visted = [0 for _ in range(n+1)] # 방문여부 초기화
    if view[i] == 0:
        continue
    dfs(i)
print(count)
