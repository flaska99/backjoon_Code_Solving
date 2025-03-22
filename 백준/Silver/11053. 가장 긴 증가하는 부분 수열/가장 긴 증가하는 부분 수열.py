import sys
def binary_search(arr, target) :
    left = 0
    right = len(arr)
    while left < right :
        mid = (left + right) // 2
        if arr[mid] < target :
            left = mid + 1
        else :
            right = mid
    return left

def lis_length():
    lis = []
    for num in num_list :
        idx = binary_search(lis, num)

        if idx == len(lis):
            lis.append(num)
        else:
            lis[idx] = num
    return print(len(lis))

t = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
lis_length()

