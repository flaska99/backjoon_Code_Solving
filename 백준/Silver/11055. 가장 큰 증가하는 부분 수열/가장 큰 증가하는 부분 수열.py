import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = A[:]  # 각 원소가 자기 자신만 포함할 때의 합으로 초기화

for i in range(1, n):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + A[i])


print(max(dp))
