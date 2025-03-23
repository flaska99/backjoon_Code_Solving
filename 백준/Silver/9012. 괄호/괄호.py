from collections import deque

t = int(input())


for i in range(t) :
    stack = deque()
    li = list(input())
    
    for i in li :
        if i == ')' and stack and stack[-1] == '(':
            stack.pop()
        
        else:
            stack.append(i)
        
    
    if len(stack) == 0 :
        print('YES')
    
    else : print('NO')