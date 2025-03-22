# 공유기가 각 최소거리로 설치되어야함
# 최소거리로 설치할수있는 범위 중
# 최대의 거리로 설치해야함.
import sys

n, c = map(int, sys.stdin.readline().split())
home_list = [int(sys.stdin.readline()) for _ in range(n)]
home_list.sort()

def can_install(min_distance) :
    count = 1
    last = home_list[0]
    for i in range(1, n) :
        if home_list[i] - last >= min_distance :
            count += 1
            last = home_list[i]
    return count >= c 

start = 1
end = home_list[-1] - home_list[0]
result = 0

while start <= end:
    mid = (start + end) // 2

    if can_install(mid):
        result = mid
        start = mid + 1
    
    else:
        end = mid -1
    
print(result)


