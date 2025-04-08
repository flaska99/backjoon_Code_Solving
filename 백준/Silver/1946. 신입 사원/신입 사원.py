import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    li = [tuple(map(int, input().split())) for _ in range(n)]

    # 서류 기준 오름차순 정렬
    li.sort()

    count = 1  # 첫 번째 사람은 무조건 통과
    best_interview = li[0][1]  # 첫 번째 사람의 면접 점수 기준

    for i in range(1, n):
        if li[i][1] < best_interview:  # 면접 순위가 더 좋다면 통과
            count += 1
            best_interview = li[i][1]

    print(count)
