
## 경로가 3개 만큼 생기고 비용이 1이라고 생각하면됨..
## 하지만 경로가 비용이 15가 될떄 까지 늘어날수있음
## 이떄 15는 횟수로 생각해도될듯
## 그리고 최소비용으로 정렬후에 
## 최소비용으로 타는bfs ? (x)

import sys
from collections import deque

input = sys.stdin.readline

n,k = map(int, input().split())
coin_list = [int(input().strip()) for _ in range(n)]

visited = [False] * (k + 1)
q = deque()
q.append((0,0))
visited[0] = True

while q :
    current, count = q.popleft()
    
    if current == k:
        print(count)
        break

    for coin in coin_list:
        next_value = current + coin
        if next_value <= k and not visited[next_value]:
            visited[next_value] = True
            q.append((next_value, count + 1))

else:
    print(-1)
