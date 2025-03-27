import sys
from collections import deque
## n의 입력값이 100 이하여서
## 문제 그대로 탐색하여 구현해도 문제 X
## O(n^2) 가능
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    n_list = list(map(int, input().split()))

    queue = deque([(priority, idx) for idx, priority in enumerate(n_list)])
    count = 0

    while queue:
        cur = queue.popleft()
        # 현재 문서보다 우선순위 높은 게 뒤에 있으면 다시 넣기
        if any(cur[0] < q[0] for q in queue):
            queue.append(cur)
        else:
            count += 1
            if cur[1] == m:

                print(count)
                break
