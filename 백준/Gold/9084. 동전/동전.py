import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    n_list = map(int, input().split())
    m = int(input())

    dp = [0] * (m+1)
    dp[0] = 1

    answer = 0

    for num in n_list :
        for i in range(num, m+1):
            dp[i] += dp[i - num]
    
    print(dp[m])