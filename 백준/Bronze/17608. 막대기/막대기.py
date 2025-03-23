from collections import deque
import sys

t = int(input())
num_list = [int(sys.stdin.readline().strip()) for _ in range(t)]

stack = deque()
for i in num_list :
    while len(stack) != 0 and stack[-1] <= i :
        stack.pop()
    stack.append(i)

print(len(stack))
