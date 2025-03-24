import sys
from collections import deque

input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.item = deque()
    
    def push(self, num):
        self.item.append(num)

    def pop(self):
        return self.item.popleft() if self.item else -1

    def size(self):
        return len(self.item)

    def empty(self):
        return 0 if self.item else 1

    def front(self):
        return self.item[0] if self.item else -1

    def back(self):
        return self.item[-1] if self.item else -1

# 입력 처리
n = int(input())
q = Queue()
output = []

for _ in range(n):
    command = input().strip()
    if command.startswith("push"):
        _, num = command.split()
        q.push(num)
    elif command == "pop":
        output.append(q.pop())
    elif command == "size":
        output.append(q.size())
    elif command == "empty":
        output.append(q.empty())
    elif command == "front":
        output.append(q.front())
    elif command == "back":
        output.append(q.back())

# 출력
sys.stdout.write('\n'.join(map(str, output)))
