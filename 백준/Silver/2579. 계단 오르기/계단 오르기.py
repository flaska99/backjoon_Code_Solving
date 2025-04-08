import sys 

input = sys.stdin.readline

n = int(input())
score = [0] + [int(input()) for _ in range(n)]  # 1-based index

dp = [0] * (n + 1)

# 초기값 처리 (계단이 1~3일 때 직접 계산)
dp[1] = score[1]
if n >= 2:
    dp[2] = score[1] + score[2]
if n >= 3:
    dp[3] = max(score[1] + score[3], score[2] + score[3])

# 점화식 적용
for i in range(4, n + 1):
    dp[i] = max(
        dp[i - 2] + score[i],
        dp[i - 3] + score[i - 1] + score[i]
    )

print(dp[n])