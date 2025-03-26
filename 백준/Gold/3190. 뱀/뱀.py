import sys
from collections import deque

class snake :
    def __init__(self):
        self.snake = deque()
        self.snake.append((0,0))

    def snake_move(self, value):
        self.snake.append(value)

    def snake_move_end(self):
        return self.snake.popleft()

input = sys.stdin.readline

n = int(input())
k = int(input())

k_list = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(k)]
l = int(input())
l_list = [tuple(input().split()) for _ in range(l)]
l_list = [(int(t), d) for t, d in l_list]

x, y, time, i  = 0,0,0,0

turn_x = (0,1,0,-1)
turn_y = (1,0,-1,0)
dummy = snake()


while True :
    time += 1 ## 시간
    
    x += turn_x[i]
    y += turn_y[i]

    # 벽 충돌 검사
    if not (0 <= x < n and 0 <= y < n):
        break

    if (x, y) in dummy.snake: 
        break

    dummy.snake_move((x,y))

    if (x, y) in k_list :
        k_list.remove((x, y))
    else :
        dummy.snake_move_end()

    if any(x == time and d == 'D' for x,d in l_list):
        i = ( i + 1 ) % 4 
    elif any(x == time and d == 'L' for x,d in l_list):
        i = ( i - 1 ) % 4    

print(time)
