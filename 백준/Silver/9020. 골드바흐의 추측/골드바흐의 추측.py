# # 2보다 큰 짝수 n이 주어졌을 때,
# # n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 
# # 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 
# # 두 소수의 차이가 가장 작은 것을 출력한다.
# # 4 <= n <= 10,000

# # 에라토스테네스의 채 함수 -> 제곱근까지 소수 리턴
# # 비교 함수 -> 소수(a) - 소수(b) 의 차가 작은걸 리턴 

# import sys

# def decimal(n) : ## 에라토스테네스의 체 (소수 분별 알고리즘)
#     is_prime = [True] * (n + 1)
#     is_prime[0], is_prime[1] = False, False

#     for i in range(2, int(n ** 0.5) + 1) :
#         if is_prime[i]:
#             for j in range(i*i, n+1, i) : #i의 배수
#                 is_prime[j] = False
#     #리스트 반환
#     return [i for i in range(2, n+1) if is_prime[i]]

# def comp(num, li) : #두 수의 합이 num일 경우 인덱스 반환
#     idx_1 = 0; idx_2 = 0
#     for i in range(len(li)) :
#         for j in range(len(li)) :
#             sum = li[i] + li[j]
#             if sum == num : 
#                 idx_1 = i; idx_2 = j
#     return [idx_1, idx_2]

# t = int(input())
# num_list = [int(sys.stdin.readline()) for _ in range(t)]

# for num in num_list :
#     decimal_list = decimal(num) # 소수 리스트 생성
#     sum_list = comp(num, decimal_list) # 두 수의 합 인덱스 반환

#     temp = decimal_list[1] - decimal_list[0] # 초기값

#     for idx_list in sum_list :
#         sub = temp
#         for j in range(len(idx_list)) :
#             idx_1 = idx_list[1]; idx_2 = idx_list[0]
#             if sub <= (decimal_list[idx_2] - decimal_list[idx_1]) :
#                 answer_idx1 = idx_1, answer_idx2 = idx_2
#                 sub = decimal_list[idx_2] - decimal_list[idx_1]

#     print(f'{answer_idx1}  {answer_idx2}')

# 위 방법 잘못 접근한듯... 다시한번...
# 차이가 적은 소수로 덧셈을 출력하는 방법 ?
# 배열에 해당 소수를 모두 넣는것은 공간적 낭비라는 생각이듦
# 또한 인덱스를 계속해서 반환해야하기떄문에 중간중간 함수 지정에 오류가 생김
# 짝수여서 반으로 나누는게 가능
# 반으로 나눈후에 조건문을 통해 소수인지 판단 후
# 둘다 소수면 출력 아니라면면
# 한쪽은 +1 , 한쪽은 -1 을 하며,
# 루프
import sys

def decimal(n) :
    if n == 1 : return False
    for i in range(2, int(n ** 0.5) + 1) :
        if n % i == 0 : return False
    return True

t = int(input())

num_list = [int(sys.stdin.readline()) for _ in range(t)]

for num in num_list :
    num_1, num_2 = num // 2 , num // 2

    while num_1 > 0 :
        if decimal(num_1) and decimal(num_2) :
            print(num_1, num_2); break
        num_1 -= 1; num_2 += 1
