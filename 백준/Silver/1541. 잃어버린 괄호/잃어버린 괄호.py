import sys
input = sys.stdin.readline

expression = input().strip()

# 1. '-'로 쪼갬
parts = expression.split('-')

# 2. 첫 번째 부분은 그냥 더함 (처음 항)
result = sum(map(int, parts[0].split('+')))

# 3. 두 번째부터는 모두 괄호처럼 묶어서 빼기
for part in parts[1:]:
    result -= sum(map(int, part.split('+')))

print(result)
