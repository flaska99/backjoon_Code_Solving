#특성값이 0에 가장 가깝다는건
# 최솟값 ?
#음수라면 최댓값값인 경우 
# 양수에서의 최솟값인 경우 
# 음수의 인덱스와 양수의 인덱스를

import sys

t = int(input())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

lp, rp = 0, t-1  #왼쪽 포인터, 오른쪽 포인터
min_range = 2_000_000_001
answer_1, answer_2 = lp, rp

while lp < rp :
    last = num_list[lp] + num_list[rp]
    
    if abs(last) < min_range :
        min_range = abs(last)
        answer_1 = lp
        answer_2 = rp

    if last < 0:
        lp += 1  
    
    else :  rp -= 1

    

print(num_list[answer_1], num_list[answer_2])
    
        

        


        
