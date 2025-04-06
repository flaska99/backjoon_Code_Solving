import sys

input = sys.stdin.readline

a = input().strip()
b = input().strip()

def lcs (x,y):
    n = len(x)
    m = len(y)

    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for ii in range(1, m+1):
            if x[i - 1] == y [ii - 1]:
                dp[i][ii] = dp[i-1][ii-1] + 1
            else:
                dp[i][ii] = max(dp[i-1][ii], dp[i][ii-1])
    
    return dp[n][m]

print(lcs(a,b))