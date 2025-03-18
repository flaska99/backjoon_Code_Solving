import sys

def bubble_sort(arr) :
    n = len(arr) - 1
    for i in range(n, 0, -1) :
        for j in range(i) :
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    



n = int(input())  # 첫 번째 입력을 정수로 받음 (배열의 크기)
num_list = [int(sys.stdin.readline().strip()) for _ in range(n)]

bubble_sort(num_list)

for i in num_list :
    print(i)
