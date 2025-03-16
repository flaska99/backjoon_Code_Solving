# 한자리 수는 무조건 한수 
# 두자리 수도 무조건 한수
# 그 다음 부터는 각 자리의 수가 등차 수열을 이루어야 한수
# 조건 ? 1. 각 자리가 작아짐 경우 2. 각 자리가 커짐
# 나누는 기준 ?  정수형바꾼후에 string을 통해 접근!
# 0번째 와 1번쨰 인덱스의 차를 구함 -> 1번째 인덱스와 그 차를 더했을때
# 2번째 인덱스일 경우 count ++
# 101 의 경우 1과 0의 차가 +1 로 반영... 
# 그럴 경우 다음 인덱스때

n = int(input()) # 하나의 요소만 입력받기 때문에 input이 적합
count = 0

for i in range(n+1) :
    if i == 0 : continue
    num = str(i)

    if len(num) == 1 or len(num) == 2 :
        count += 1; continue
    
    temp = int(num[1]) - int(num[0]) # 두 수의 차

    for j in range(1, len(num) - 1) :
        if int(num[j + 1]) != int(num[j]) + temp : break 
        # 아닐때 루프문 터트리기(검사 할 필요가 없음)  
    else : count += 1
print(count)
            
