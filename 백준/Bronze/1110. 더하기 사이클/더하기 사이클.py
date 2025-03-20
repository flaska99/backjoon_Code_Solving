
# 풀지못했습니다..

# 0보다 크거나같고 99보다 작거나 같은 정수가 주어짐
# 먼저 주어진 수가 10보다 작다면 0을 붙여 두자리 수 만들고
# 각자리의 숫자를 더함

#주어진 수의 첫번째 가장 오른쪽 자리 수와 
# 앞에서  구한 합의 가장 오른쪽 자리수를 이어 붙여 새로운 수 만듦

#26 = 2+6 = 8, 새로운 수 는 68 , 6+8 = 14 새로운 수 84,
# 8+ 4 = 12 , 새로운 수 26 
# 원래 수로 돌아오는 사이클

#55의 경우 시간초과가 발생함..
def number(n) :
    n = int(n)
    
    # 코드 오류의 원흉... 주석 생활화 합시다.
    # if n < 10 :
    #     n = n * 10

    n_1 = n % 10 #둘째 자리
    sum = n_1 + (n // 10)

    if sum >= 10 :  
        n_2 = sum % 10
    else : 
        n_2 = sum

    if(n_1 == 0):
        new_num = n_2
    else : new_num = str(n_1) + str(n_2)

    return new_num
    

n = int(input())
count = 0
temp = n


while True :
    temp = number(temp) # 한사이클 끝 temp에 들어간건 new_num
    count += 1

    if (n == int(temp)) :
        break

print(count)