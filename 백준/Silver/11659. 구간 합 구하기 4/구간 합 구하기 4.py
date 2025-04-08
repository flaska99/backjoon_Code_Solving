import sys
input = sys.stdin.readline

n, m = map(int, input().split())
i_list = list(map(int, input().split()))

# 누적합 배열 만들기 (길이: n+1)
prefix = [0] * (n + 1)

for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + i_list[i - 1]

# 질의 처리
for _ in range(m):
    x, y = map(int, input().split())
    print(prefix[y] - prefix[x - 1])
