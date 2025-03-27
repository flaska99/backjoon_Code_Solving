import sys

def solve(left, right, target) :
    while left <= right:
            mid = (left + right) // 2
            if n_list[mid] == target:
                return True
            elif n_list[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    return False

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

view = [0] * m

n_list.sort() # target 내림차순 정렬

for i in range(len(m_list)):
    if solve(0, n - 1, m_list[i]):
        view[i] = 1

for i in view :
    print(i, end= " ")




