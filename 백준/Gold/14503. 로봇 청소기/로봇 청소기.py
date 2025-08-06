from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, dir = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def robot_moved(graph, r, c, dir):
    count = 0
    # 북 동 남 서
    dir_x = [-1, 0, 1, 0]
    dir_y = [0, 1, 0, -1]

    robot = deque()
    robot.append((r, c, dir))

    while robot:
        x, y, direction = robot.popleft()

        # 현재 칸 청소
        if graph[x][y] == 0:
            graph[x][y] = 2
            count += 1

        moved = False

        for _ in range(4):
            direction = (direction + 3) % 4
            dx = x + dir_x[direction]
            dy = y + dir_y[direction]

            if 0 <= dx < n and 0 <= dy < m and graph[dx][dy] == 0:
                robot.append((dx, dy, direction))
                moved = True
                break

        # 벽인 경우 후진
        if not moved:
            back_dir = (direction + 2) % 4
            bx = x + dir_x[back_dir]
            by = y + dir_y[back_dir]

            if 0 <= bx < n and 0 <= by < m and graph[bx][by] != 1:
                robot.append((bx, by, direction))
            else:
                break

    return count

print(robot_moved(graph, r, c, dir))
