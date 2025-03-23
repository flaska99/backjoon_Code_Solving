import sys

def divide_mod (a, b, c) :
    if b == 0 :
        return 1

    half = divide_mod(a, b// 2, c)

    result = (half * half) % c

    if b % 2 == 1 :
        result = (result * a) % c

    return result

a,b,c = map(int, sys.stdin.readline().split())

print(divide_mod(a, b, c))


