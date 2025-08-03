from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        combs = []
        for order in orders:
            order = ''.join(sorted(order))  
            combs += combinations(order, c)
        comb_counter = Counter(combs)
        print(combs)
        print(comb_counter.items())
        
        if not comb_counter:
            continue
        
        max_count = max(comb_counter.values())
        
        # 최소 2명 이상이 주문한 경우만 포함
        if max_count < 2:
            continue
        
        for comb, cnt in comb_counter.items():
            if cnt == max_count:
                answer.append(''.join(comb))
                
    return sorted(answer)