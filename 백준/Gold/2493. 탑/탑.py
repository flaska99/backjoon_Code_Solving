import sys

input = sys.stdin.readline
n = int(input())
heights = list(map(int, input().split()))
stack = []
answer = []

for i in range(n):
    while stack and stack[-1][1] < heights[i]:
        stack.pop()
    
    if not stack:
        answer.append(0)
    else:
        answer.append(stack[-1][0])
    
    stack.append((i + 1, heights[i]))  # (탑 번호, 높이)

print(" ".join(map(str, answer)))
