import sys
class max_heap :
    def __init__(self):
        self.heap = []
    
    def push(self, value) :
        
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop(self) :
        if self._is_empty() :
            return 0
        if len(self.heap) == 1 :
            return self.heap.pop()

        root_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root_value

    def _heapify_up(self, idx):
        parent = (idx-1) // 2

        if idx > 0 and self.heap[idx] > self.heap[parent] :
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            return self._heapify_up(parent)
        
    def _heapify_down(self, idx):
        while True :    
            left = (idx * 2) + 1
            right = (idx * 2) + 2
            largest = idx

        
            if left < len(self.heap) and self.heap[left] > self.heap[largest] :
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest] :
                largest = right
            
            if largest == idx :
                break

            self.heap[largest], self.heap[idx] = self.heap[idx], self.heap[largest]
            idx = largest
    
    def _is_empty(self) :
        return not self.heap

n = int(input())
m = [int(sys.stdin.readline().strip()) for _ in range(n)]
heap = max_heap()

for i in m :
    if i == 0 :
        print(heap.pop())
    else :
        heap.push(i)