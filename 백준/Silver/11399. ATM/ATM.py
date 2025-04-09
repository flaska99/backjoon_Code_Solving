import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))


n_list.sort()
dp = [0] * (n+1)

for i in range(1,n+1):
    dp[i] = dp[i-1] + n_list[i-1]

print(sum(dp))