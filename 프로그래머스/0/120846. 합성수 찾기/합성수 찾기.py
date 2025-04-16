def solution(n):
    answer = 0  
    for i in range(4, n+1):
        count = 0
        for ii in range(1,n+1):
            if i%ii == 0 :
                count += 1
        
        if count >= 3:
            answer += 1
    
    return answer