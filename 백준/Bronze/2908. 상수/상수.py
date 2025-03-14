import sys
before = sys.stdin.readline().split()
after = [before[i][::-1] for i in range(2)]
print(after[0] if after[0] > after[1] else after[1])