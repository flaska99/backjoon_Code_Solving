import sys

t = int(input())
word_list = [sys.stdin.readline().strip() for _ in range(t)]

## sort함수 주의점 
# 만약 조건을 걸시에 a, b 조건이 있으면
# b조건 충족 후 a 정렬을 해야함

word_list = list(set(word_list)) ## set함수를 사용하여 중복제거거
word_list.sort() # b 조건 충족 (단어 순 정렬)
word_list.sort(key=len)# c 조건 충족 (길이 순 정렬)
for i in word_list : print(i)