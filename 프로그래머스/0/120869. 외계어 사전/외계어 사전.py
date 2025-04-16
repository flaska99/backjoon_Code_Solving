def solution(spell, dic):
    answer = 2
    count = 0
    for temp in dic:
        count = 0
        for ch in spell:
            if ch in temp:
                count += 1
        if count == len(spell):
            answer = 1
    
    return answer