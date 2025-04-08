import sys

input = sys.stdin.readline

n, m= map(int, input().split())

n_list = [int(input()) for _ in range(n)]


dp = [0] * (m+1)
dp[0] = 1

answer = 0

for num in n_list :
    for i in range(num, m+1):
        dp[i] += dp[i - num]

print(dp[m])
