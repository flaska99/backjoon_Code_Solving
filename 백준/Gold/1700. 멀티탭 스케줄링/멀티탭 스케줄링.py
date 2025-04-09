import sys

input = sys.stdin.readline

n, k = map(int, input().split())

n_list = list(map(int, input().split()))

answer = [] 
count = 0    # 교체 횟수

for i in range(k):
    current = n_list[i]

    if current in answer:
        continue

    
    if len(answer) < n:
        answer.append(current)
        continue

    farthest_idx = -1
    to_remove = -1

    for idx, item in enumerate(answer):
        try:
            next_use = n_list[i+1:].index(item)
        except ValueError:
            next_use = float('inf')  

        if next_use > farthest_idx:
            farthest_idx = next_use
            to_remove = idx

    answer[to_remove] = current
    count += 1

print(count)

