# 이전코드
# 문자열 출력에 대한 오류
# 왜 ? for문을 통한 출력에 대한 생각 교착
# 어떻게 해결 ? 
# 알고리즘을 돌고 나온 코드를 바로 print를 통해 출력해주지 않고
# answer = '' => 빈 문자열 변수를 루프마다 초기화 시키며 해당 변수에 담아서 출력
# import sys

# t = int(sys.stdin.readline())

# for _ in range(t) : 
#     num_list = sys.stdin.readline().split() # ['3', 'ABC']
#     char = [char for char in num_list[1]] # ['A', 'B', 'C']
#     for i in char : 
#         print(i * int(num_list[0]), end="")
#     print("\n")

import sys

t = int(sys.stdin.readline())
for _ in range(t) :
    answer=''
    num_list = sys.stdin.readline().split() # ['3', 'ABC']
    char = [char for char in num_list[1]] # ['A', 'B', 'C']
    for i in char : 
        answer += i * int(num_list[0])
    print(answer)
    
