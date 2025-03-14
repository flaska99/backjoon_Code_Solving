#이 코드 시간 초과됨 
#다시봐도 코드가 너무 무식함
# import sys
# a, b, v = map(int, sys.stdin.readline().split())
# snail_work = 0; day_count = 1 # 첫날 = 1일

# while True :
#     snail_work += a
#     if snail_work >= v : break 
#     # 크거나 같을 때 *같기만 하는 조건으로 했다가 무한교착에 빠져버림...
#     snail_work -= b ; day_count += 1 

# print(day_count)

# 수학적 로직으로 접근해봄
# 하루의 순 상승량 : a - b 
# 목표량 / 하루의 순 상승량 = 소요 날짜
# 목표량 % 하루의 순 상승량
# 목표량의 나머지가 O 소요날짜 + b
# 목표량의 나머지가 있음 소요날짜 - b
# 왜 ? 목표량을 순 상승량으로 나누면 몫이 소요날짜다
# 나머지가 있다면 다음날 순상승량이 아닌 a의 값으로 다음날 등반에 성공한 것이다.
# 간단히 말하면 마지막 날(등반 성공한 날)은 미끄러지지않으니 결과값에 - b를
# 따라서 식을 세우면 (v - b) / (a - b)이다.
# day = 0 

# 하지만 해당과정도 망함
# import sys
# a, b, v = map(int, sys.stdin.readline().split())
# snail_work = a - b # 하루의 순 상승량
# success = v - b

# print(success // snail_work)

# 하루의 순 상승량 : a - b 
# 목표량 // 하루의 순 상승량 = 소요 날짜 (몫)
# 목표량 % 하루의 순 상승량 :
# 나머지(O) : 밑에 조건문으로 나머지(X) : 목표량 // 하루의 순 상승량
# 나머지와 a(달팽이가 올라갈 수 있는 거리)를 비교해봄

import sys
a, b, v = map(int, sys.stdin.readline().split())
day = (v - b) // (a - b)  #소요 날짜 (몫) 
remain = (v - b) % (a - b) # 나머지
print(day if remain == 0 else day+1)
# 마지막 날은 내려가지 않으니 -b를 해줘야한다.

# 내일 다시 풀어보자... 나머지가 있을시에 + 1
# import sys
# import math
# a, b, v = map(int, sys.stdin.readline().split())
# 마지막 날에는 미끄러지지 않으므로 (V - B)를 기준으로 계산
# day = math.ceil()) 
# ceil는 언제나 올림을 함
# print(day)