def dfs(n) :
    global ans
    if n == N: # N행 까지 진행한 경우에 성공
        ans += 1
        return
    
    for j in range(N):
        if v1[j] == v2[n+j] == v3[n-j] == 0 : #놓을 수 있는 경우
            v1[j] = v2[n+j] = v3[n-j] = 1
            dfs(n+1)
            v1[j] = v2[n+j] = v3[n-j] = 0

N = int(input())

ans = 0
v1 = [0] * N ## 가로, 세로
v2 = [0] * (2*N) # 
v3 = [0] * (2*N)
dfs(0)
print(ans)