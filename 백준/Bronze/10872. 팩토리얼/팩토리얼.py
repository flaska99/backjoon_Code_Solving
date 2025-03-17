n = int(input())
pac = 1
for i in range(1, n+1) : pac *= i

print('1' if n == 0 else pac)