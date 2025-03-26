import math

def solution(progresses, speeds):
    count = 0
    answer = []
    
    for i in range(len(speeds)):
        n = math.ceil((100 - progresses[i]) / speeds[i])
        if i == 0 :
            temp = n
        
        if temp >= n:
            count += 1
            continue
        
        else :
            answer.append(count)
            count = 1
            temp = n
    
    answer.append(count)
    
    return(answer)