import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n)]

# 초기값: 0번 집의 색별 비용
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

# 1번 집부터 시작해서 순차적으로 계산
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]


# 마지막 집을 어떤 색으로 칠했든 최소값이 답
print(min(dp[n-1]))
