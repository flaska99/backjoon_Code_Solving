from collections import deque
import sys

t = int(input())

stack = deque()

num_list = [int(sys.stdin.readline().strip()) for _ in range(t)]

for i in range(t) :
    if num_list[i] == 0 :
        stack.pop()
        
    
    else :
        stack.append(num_list[i])
    

print(sum(stack))