# 두번 뽑고, 서로 더한다
# 더한것을 힙에 넣고, sum에도 저장
# 반복

# 재귀 ? -> 기저조건은 ?
import sys, heapq

input = sys.stdin.readline

n = int(input())
total = 0
li = [int(input()) for _ in range(n)]
heapq.heapify(li)

while len(li) > 1 :
    num_1 = heapq.heappop(li)
    num_2 = heapq.heappop(li)
    merged = num_1 + num_2
    total += merged

    heapq.heappush(li, merged)

print(total)