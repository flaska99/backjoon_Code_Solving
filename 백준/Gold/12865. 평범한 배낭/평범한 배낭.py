import sys
input = sys.stdin.readline

n, k = map(int, input().split())  # 물건 수, 최대 무게

items = []
for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

# dp[i]: 무게 i까지 담을 수 있을 때 얻을 수 있는 최대 가치
dp = [0] * (k + 1)

for w, v in items:
    # 거꾸로 순회해야 "한 번만 쓴다"는 조건이 만족됨 (0-1 배낭)
    for i in range(k, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)

print(dp[k])

    




