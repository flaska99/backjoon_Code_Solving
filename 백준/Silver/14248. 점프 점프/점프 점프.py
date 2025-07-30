from collections import deque

def count_reachable_stones(n, A, s):
    visited = [False] * n
    queue = deque()

    queue.append(s - 1)
    visited[s - 1] = True

    while queue:
        current = queue.popleft()
        jump = A[current]

        for next_pos in [current + jump, current - jump]:
            if 0 <= next_pos < n and not visited[next_pos]:
                visited[next_pos] = True
                queue.append(next_pos)

    return sum(visited)

n = int(input())
A = list(map(int, input().split()))
s = int(input())

print(count_reachable_stones(n, A, s))
