# n의 개수가 많아짐 시간복잡도가 적은것으로
# n < = m
import sys

def solve(arr, target, left, right):
    if left > right:
        return 0

    mid = (left + right) // 2

    if arr[mid] == target:
        return 1
    elif arr[mid] < target:
        return solve(arr, target, mid + 1, right)
    else:
        return solve(arr, target, left, mid - 1)



n = int(input())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(input())
m_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()
for j in m_list :
    print(solve(n_list, j, 0, n - 1))