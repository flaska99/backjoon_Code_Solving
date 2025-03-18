#재귀를 생각해봅시다.
#재귀함수를 잘 구현하게 된다면
# 본인은 함수 안에 함수들이 다 처리 된후 
# 마지막 값을 처리하는 느낌으로 이해함

# 그럼 제일 컷을 때 n값을 처리하고 
# 계속 2^(n-1)로 줄여가서
# 재귀에서 제일 깊은 함수가 2^1 배열을 처리하는 것

import sys

def z(num, m, n) :
    
    if num  == 0 :
        return 0
    
    half = 2 ** (num  - 1) ## 반으로 나눳을때 사분면을 나눌 기준
    size = half * half # 한 사분면에 포함되는 원소의 개수
# half = 2 size = 4 (3,1) -> (1, 1, 1) + 8
# half = 1 size = 1 (1,1) -> 3
    if m < half and n < half : # 좌상 사분면
        return z(num-1, m, n)
    elif m < half and n >= half : # 우상 
        return size + z(num -1, m, n - half)
    elif m >= half and n < half : # 좌하
        return 2 * size + z(num -1, m - half, n)
    elif m >= half and n >= half :
        return 3 * size + z(num -1, m - half, n - half) # 우하
    
num, m, n = map(int, sys.stdin.readline().split())
print(z(num, m ,n))