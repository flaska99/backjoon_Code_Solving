import sys

def merge_sort(arr) :
    if len(arr) < 2 : return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[mid:])
    right_arr = merge_sort(arr[:mid])

    merged_arr = []

    left = right = 0

    while left < len(left_arr) and right < len(right_arr) :
        if left_arr[left] < right_arr[right] :
            merged_arr.append(left_arr[left])
            left += 1
        
        else :
            merged_arr.append(right_arr[right])
            right += 1

    merged_arr += left_arr[left:]
    merged_arr += right_arr[right:]

    return merged_arr


t = int(input())
num_list = merge_sort([int(sys.stdin.readline()) for _ in range(t)])
for n in num_list : print(n)