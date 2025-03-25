import heapq, sys

n = int(input())
left_heap = [] # 최대힙
right_heap = [] #최소힙

for i in range(n) :
    num = int(sys.stdin.readline())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    
    else :
        heapq.heappush(right_heap, num)
    
    if right_heap and right_heap[0] < -left_heap[0] :
        left_value = heapq.heappop(left_heap)
        right_value = heapq.heappop(right_heap)

        heapq.heappush(left_heap, -right_value)
        heapq.heappush(right_heap, -left_value)
    
    print(-left_heap[0])