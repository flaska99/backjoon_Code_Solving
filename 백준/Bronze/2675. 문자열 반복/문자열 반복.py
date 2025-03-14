import sys

t = int(sys.stdin.readline())
for _ in range(t) :
    answer=''
    num_list = sys.stdin.readline().split() # ['3', 'ABC']
    char = [char for char in num_list[1]] # ['A', 'B', 'C']
    for i in char : 
        answer += i * int(num_list[0])
    print(answer)
    