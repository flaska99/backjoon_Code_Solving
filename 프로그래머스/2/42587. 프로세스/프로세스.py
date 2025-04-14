from collections import deque

def solution(priorities, location):
    q = deque()
    
    for i in range(len(priorities)):
        q.append((i, priorities[i]))
        
    count = 0
    while q: 
        index, p = q.popleft()
        if any(p < other_p for _, other_p in q):
            q.append((index, p))
        else:
            count += 1
            if index == location:
                return count