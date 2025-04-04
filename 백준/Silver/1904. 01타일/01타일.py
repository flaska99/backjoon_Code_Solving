n = int(input())
MOD = 15746


a, b = 1, 2  # dp[1], dp[2]

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    for _ in range(3, n + 1):
        a, b = b, (a + b) % MOD
    print(b)
