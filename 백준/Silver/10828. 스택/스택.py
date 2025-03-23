import sys

class stack :
    def __init__(self):
        self.items = []
    
    def push(self, number) :
        self.items.append(number)
    
    def pop(self) :
        if not self.items :
            print('-1')
        
        else : 
            print(self.items[len(self.items) - 1])
            self.items = self.items[:len(self.items) - 1]

    def top(self) :
        if not self.items :
            print('-1')
        
        else :
            print(self.items[len(self.items) - 1])

    def empty(self) :
        if not self.items :
            print('1')

        else :
            print('0')     

    def size(self) :
        if not self.items :
            print('0')
        else :
            print(len(self.items))   

n = int(input())
order_list = [sys.stdin.readline() for _ in range(n)]
stack_exam = stack()

for i in range(n) :
    if order_list[i].find('push') == 0 :
        m, n = order_list[i].split()

        stack_exam.push(n)
    
    elif order_list[i].find('pop') == 0 :
        stack_exam.pop()

    elif order_list[i].find('top') == 0 :
        stack_exam.top()

    elif order_list[i].find('size') == 0 :
        stack_exam.size()

    elif order_list[i].find('empty') == 0 :
        stack_exam.empty()




