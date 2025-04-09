import sys

input = sys.stdin.readline

n = int(input())

k_list = [-int(input()) for _ in range(n)]
k_list.sort()


maximum = -k_list[0]
for i in range(1, n):
    maximum = max(maximum, -(k_list[i]) * (i+1))

print(maximum)
