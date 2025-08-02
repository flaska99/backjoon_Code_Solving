# 일정금액을 지불하면 10일 동안 회원 자격을 부여함.
# XYZ 마트에서는 회원을 대상으로 매일 한가지 제품을 할인하는 행사를 함.
# 해당 제품은 하루 1개 구매 가능
# 그래서 자신이 원하는 제품과 할인 하는 날짜가 10일 동안 일치할 경우를 맞춰서
# 회원 가입을 진행하려고함.

# WANT : 정현이가 원하는 제품 
# NUMBER : 제품 개수 (동 제품 동 INDEX)
# DISCOUNT : 할인 제품 (하루 1개만 구입 가능)

# 다 구입 가능한 날짜를 찾아야함. 만약 불가능 하다면 0 반환
# 회원 등록은 10일 동안 지속가능

from collections import deque, Counter

def solution(want, number, discount):
    want_dict = dict(zip(want, number))
    cnt = 0
    dq = deque(discount[:10])
    
    for i in range(len(discount) - 9):
      
        cur_window = Counter(dq)
        
      
        if all(cur_window[item] == want_dict.get(item, 0) for item in want_dict):
            cnt += 1
        
       
        if i + 10 < len(discount):
            dq.popleft()
            dq.append(discount[i + 10])
    
    return cnt
