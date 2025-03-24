from collections import deque

def check_card(li) :
    while len(li) > 1 :
        li.popleft()
        li.append(li.popleft())
    return li[0]
        

n_list = [i for i in range(1, int(input()) + 1)]
queue = deque(n_list)
print(check_card(queue))