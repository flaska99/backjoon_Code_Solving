# import sys, heapq
# from collections import deque

# def search_virus(map, li):
#     virus_list = []
#     for i in range(n):
#         for ii in range(n):
#             if map[i][ii] != 0:
#                 li.append((map[i][ii],i,ii))
#     return virus_list

# def bfs(graph, li, dx, dy):
#     time = 0 
#     while li:
#         if time == s:
#             break
#         virus_index, x, y = li.popleft()

#         for i in range(4):
#             nx = dx[i] + x
#             ny = dy[i] + y

#             if 0 <= nx < n and 0<= ny < n and graph[nx][ny] == 0:
#                 graph[nx][ny] = virus_index
#                 li.append((virus_index, nx,ny))
            
#         if virus_index == k:
#             time += 1

# input = sys.stdin.readline
# n,k = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# que = deque()
# s, x, y = map(int, input().split())
# dx = [1,-1,0,0]
# dy = [0,0,-1,1]

# ## (우선순위, 행좌표, 열좌표)
# search_virus(graph, que)
# bfs(graph, que, dx, dy)
# print(graph[x-1][y-1])


import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, target_x, target_y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 초기 바이러스 정보 (바이러스 번호, 시간, x, y)
virus_data = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus_data.append((graph[i][j], 0, i, j))  # 바이러스 번호, 시간, 위치

# 번호가 낮은 바이러스가 먼저 퍼지도록 정렬
virus_data.sort()
queue = deque(virus_data)

# BFS
while queue:
    virus, time, x, y = queue.popleft()

    if time == s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = virus
            queue.append((virus, time + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])
