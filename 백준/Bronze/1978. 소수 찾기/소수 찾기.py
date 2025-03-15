# import sys

# t = input()
# answer = 0
# num_list = list(map(int, sys.stdin.readline().split()))
#소수 판정 ?
#소수는 1과 자기자신만 있는 수임
#num을 1 ~ 9로 나누었을때
#나머지가 0인 수가 있다면 count++
# 첫번째 루프를 돌때 count가 3개 이상이라면 루프 중지
# 해당 코드는 num % i 가 큰수에서 작은수를 나눈다는 가정이 없어 문제가있음
# for num in num_list :
#     count = 0
#     for i in range(1000) : 
#         if num % i == 0 : count += 1
#         if count >= 3 : break
#     if count == 2 and num == 1 : answer.append(num)

# print(answer)

#소수 판정 알고리즘 : 에라토스테네스의 채
#소수를 판별할 수들을 모두 써넣은 후에
# 소수도, 합성수도 아닌 유일한 자연수 '1' 을 제거
#2를 제외한 2의배수도 제거
#3을 제외한 3의배수도 제거
#4의 배수는 2의 배수에서 이미 지워졌기 떄문에 
#5를 제외한 5의 배수 제거
#(6도제외) 7을 제외한 7의 배수도 제거
#마지막으로 11을 제외한 11의 배수를 제거하면 소수만 판별가능
#무식해보이지만 에라토스테네스의 채보다 빠른방법이 없음
#하지만 제곱근을 이용해 시간복잡도를 줄이는 방법은 있다.
#근데 이 문제는 적용이 안될꺼같음
#그럼 해당 알고리즘을 이 문제에 적용해보자
# 1같은 경우는 바로 조건을 이용하여 예외로 스킵킵
#리스트에 있는 숫자가 (2,3,5,7,11) 과 나눳을때 
#나머지가 0인 숫자는 소수가 아님 => 11보다 클경우에만 판별
#11이하의 수는 리스트의 있는 숫자와 같다면 리턴
#위 조건을 제외한 수들을 출력

import sys

t = input()
num_list = list(map(int, sys.stdin.readline().split()))
count = 0 

for num in num_list :
    bool = 0
    if num == 0 or num == 1 : continue
    elif num == 2 or num == 3: count += 1; continue

    for j in range(2, num) :
        if num % j == 0 : 
            bool = 1; break

    if bool == 1 : 
        continue
    count += 1

print(count)
