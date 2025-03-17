# n = int(input())
# pac = 1
# for i in range(1, n+1) : pac *= i

# print('1' if n == 0 else pac)

# 재귀로 구현
def fac(n) :
  if n <= 1 :
    return 1
  else :
    return n * fac(n-1)

a = int(input())
print(fac(a))