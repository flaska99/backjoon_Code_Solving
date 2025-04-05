from collections import deque


def solution(numbers, target):
    que = deque()
    que.append((0, 0))

    answer = 0
    
    while que:
        sum, count = que.popleft()
        
        if count < len(numbers):
            que.append((sum + numbers[count], count + 1))
            que.append((sum - numbers[count], count + 1))
        
        if count == len(numbers) and sum == target:
            answer += 1
        
        
            
    return answer
        
        
        
        
        
        
        
    
    