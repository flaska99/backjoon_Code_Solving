def hanoi(start, end, mid, n, answer):
    if(n == 1):
        answer.append([start, end])
    else:
        hanoi(start, mid, end, n-1, answer)
        hanoi(start, end, mid, 1, answer)
        hanoi(mid, end, start, n-1, answer)
    
    
def solution(n):
    answer = []
    hanoi(1, 3, 2, n, answer)

    return answer