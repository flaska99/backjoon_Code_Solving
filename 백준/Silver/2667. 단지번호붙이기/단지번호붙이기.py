
## 시간 부족... 
## 그냥 선형 탐색이든 dfs를 돌려서
## '1' 인 곳을 찾음... 그리고 bfs 해서 그래프에 탐색 완료 마킹..
## bfs가 끝나는 지점은 한 단지의 붙어있는 1을 다 탐색한 경우
# ## bfs가 끝날때 마다 count += 1


import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

n_list = [list(map(int, input().strip())) for _ in range(n)]
answer_list = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    count = 1
    que = deque()
    que.append((x,y))
    n_list[x][y] = -1  # 시작점 방문 처리

    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0 <= ny < n and n_list[nx][ny] == 1:
                que.append((nx,ny))
                n_list[nx][ny] = -1  # 방문 처리
                count+=1

    return count

for i in range(n):
    for ii in range(n):
        if n_list[i][ii] == 1:
            answer_list.append(bfs(i, ii))


answer_list.sort()

print(len(answer_list))

for num in answer_list:
    print(num)


# print(n_list)

# 2667 단지 번호 붙이기
# 미완성 코드

