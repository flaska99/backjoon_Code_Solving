#처음점, 잘린점, 끝점을 각각 넣고
# sort함수를 통해 오름차순으로 정렬
# 오름차순으로 정렬하면 처음점, 잘린점, 끝점이 순서대로 나오게됨
# 해당 순서대로 넣고
# 앞의 인덱스랑 뺴주는 루프를 쓰면
#  잘린 만큼의 수가 나오게됨

import sys

w, h = map(int, sys.stdin.readline().split())


w_list = [0, w]
h_list = [0, h]

#초기 좌표 설정

for _ in range(int(input())) :
    a, num = map(int, sys.stdin.readline().split())

    if a == 1 : w_list.append(num)

    else : h_list.append(num)


w_list.sort(); h_list.sort()      
print(
    max([w_list[i+1] - w_list[i] for i in range(len(w_list) - 1)])
    *
    max([h_list[i+1] - h_list[i] for i in range(len(h_list) - 1)])
)