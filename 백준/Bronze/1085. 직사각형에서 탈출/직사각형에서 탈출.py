x,y,w,h = map(int, input().split())
num_1 = w - x; num_2 = h - y
print(min(num_1, num_2, x, y))