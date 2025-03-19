import sys
from itertools import permutations
n = int(input())

num_list = list(map(int, sys.stdin.readline().split()))
p = list(permutations(num_list, n))

answer = 0

for i in p:
    sum = 0
    for j in range(n-1):
        sum += abs(i[j] - i[j+1])

    answer = max(answer, sum)

print(answer)