from collections import deque
import sys
def yosepus(li, num) :
    global answer
    while len(li) > 0 :
        for _ in range(num - 1):
            li.append(li.popleft())
        answer.append(li.popleft())

    return answer
    

n, m = map(int, sys.stdin.readline().split())
answer = []
num_list = [i for i in range(1, n+1)]

num_list = deque(num_list)
yosepus(num_list, m)
print("<", end="")

for i in range(len(answer)) :
    if i == len(answer) - 1 :
        print(answer[i], end="")
    else :
        print(answer[i], end = ", ")
print(">")


