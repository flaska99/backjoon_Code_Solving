# 이거 스플릿 써도 되나 ?
# 에러 헨들링으로 FRULA 출력...
# 차력쇼 실패

# import sys

# input = sys.stdin.readline

# string = input().strip()
# a = input().strip()
# answer = string.split(a)

# if len(answer) == 1 :
#     print(answer[0])

# else:   
#     while len(answer) > 1:
#         temp = ''
#         for st in answer:
#                 temp += st
#         answer = temp.split(a)

#     if not temp: print('FRULA')
#     else : print(temp)


import sys
def string_explosion(target, bomb) :
    stack = []
    bomb_length = len(bomb)

    for char in target:
        stack.append(char)
        if ''.join(stack[-bomb_length:]) == bomb:
            del stack[-bomb_length:]
        
    result = ''.join(stack)
    return result if result else 'FRULA'

input = sys.stdin.readline

target_string = input().strip()
bomb_string = input().strip()

print(string_explosion(target_string, bomb_string))
