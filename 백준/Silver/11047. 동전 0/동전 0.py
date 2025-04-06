import sys

input = sys.stdin.readline

n, k = map(int, input().split())

m_list = [-int(input()) for _ in range(n)]
m_list.sort()


def greedy(k, m_list):
    count = 0

    for m in m_list :
        if -m <= k :
            count += k // -m
            k %= -m
        
        if k == 0:
            return count

print(greedy(k, m_list))