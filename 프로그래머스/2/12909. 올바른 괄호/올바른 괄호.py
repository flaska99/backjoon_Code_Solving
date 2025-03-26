from collections import deque

def solution(s):
    a = deque()
    
    for i in s :
        if i == '(' :
            a.append(i)
        elif i == ')':
            if len(a) == 0:
                return False  
            a.pop()

    return len(a) == 0
