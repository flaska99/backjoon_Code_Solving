import sys

input = sys.stdin.readline

n = int(input())

p = []

for _ in range(n):
    r, c = map(int, input().split())
    if not p:
        p.append(r)
    p.append(c)

dp = [[0] * n for _ in range(n)]

for length in range(2, n+1):
    for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1]
            dp[i][j] = min(dp[i][j], cost)

print(dp[0][n-1])
# dp[i][j] = 
# i ~ j 까지 행렬 곱할때 최소연산 횟수