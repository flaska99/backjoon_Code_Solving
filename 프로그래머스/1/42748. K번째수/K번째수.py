def solution(array, commands):
    answer = []
    
    for num_li in commands:
        li = array[num_li[0]-1:num_li[1]]
        print(li)
        li.sort()
        answer.append(li[num_li[2]-1])
    
    return answer
    
    