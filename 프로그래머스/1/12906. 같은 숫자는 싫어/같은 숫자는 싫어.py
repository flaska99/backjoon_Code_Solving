def solution(arr):
    answer = []
    for i in range(len(arr)) :
        
        
        if i == 0 :
            answer.append(arr[i])
            num = arr[i]
            
        if arr[i] != num :
            answer.append(arr[i])
            num = arr[i]
            
    return answer