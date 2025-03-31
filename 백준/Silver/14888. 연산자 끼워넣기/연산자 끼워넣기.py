import sys

input = sys.stdin.readline

n = int(input())

n_list = list(map(int, input().split()))
cal_table = list(map(int, input().split()))
## 0 : + || 1: - || 2: * || 3: //
## 나눗셈은 몫만
##음수인 값이 있을때는 그값을 양수로 바꾸고 몫을 음수로 다시 바꾼다
max_result = -1_000_000_000
min_result = 1_000_000_000

def dfs (index, result) :
    global max_result, min_result

    if index == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    
    for i in range(4):
        if cal_table[i] > 0:
            cal_table[i] -= 1

            if i ==0:
                dfs(index + 1, result + n_list[index])
            elif i == 1:
                dfs(index + 1, result - n_list[index])
            elif i == 2:
                dfs(index + 1, result * n_list[index])
            elif i == 3:
                if result < 0:
                    dfs(index + 1, -(-result // n_list[index]))
                else:
                    dfs(index + 1, result // n_list[index])
            cal_table[i] += 1

dfs(1, n_list[0])
print(max_result)
print(min_result)
