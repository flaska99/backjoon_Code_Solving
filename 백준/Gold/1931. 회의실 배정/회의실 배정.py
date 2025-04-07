import sys
input = sys.stdin.readline


n = int(input())

meetings = []

for i in range(n):
    x, y = map(int, input().split())
    meetings.append((x,y))

# 끝나는 시간, 시작 시간 순으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))
count = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end

print(count)


