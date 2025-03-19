import sys

li = [int(sys.stdin.readline().strip()) for _ in range(9)]
li.sort()
num = sum(li)
idx_1 = idx_2 = 0 # 인덱스 초기값
answer = []
for i in range(8) :
    for j in range(i+1, 9) :
        temp = num
        temp -= li[i] + li[j]
        if temp == 100 :
            idx_1 = i; idx_2 = j
    

for i in range(9) :
    if i == idx_1 or i == idx_2:
        continue
    print(li[i])