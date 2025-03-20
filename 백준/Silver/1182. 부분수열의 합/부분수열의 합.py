import sys

def dfs(start) :
    global answer

    if sum(v1) == s and len(v1) > 0 : # 부분집합 제거와, 합 기저조건
        answer += 1
    
    for i in range(start, n):
        v1.append(num_list[i])
        dfs(i+1)
        v1.pop() # 백트래킹

answer = 0
n, s = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
v1 = []
dfs(0)
print(answer)