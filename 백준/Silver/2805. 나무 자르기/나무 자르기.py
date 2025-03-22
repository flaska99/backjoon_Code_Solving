# n은 나무 수 
# m은 가져가야하는 나무 길이
#우리는 절단기의 설정할 수 있는 높이의 최댓값을 출력해야한다.

# 변수의 범위가 크기때문에 시간복잡도가 작은 탐색을 해야함
# nlogn -> 이분탐색 

import sys

def cut_tree(cutting) :
    tree_sum = 0
    for tree in tree_list:
        if tree > cutting:
            tree_sum += tree - cutting
    return tree_sum


def find_cut_height(start, end, target) :
    #초기값 start = 1 , end = 원소의 최댓값

    if start > end :
        return end
    
    mid = (start + end) // 2
    my_tree = cut_tree(mid)
    
    if my_tree >= target :
        return find_cut_height(mid+1, end, target)
    
    else : 
        return find_cut_height(start, mid-1, target)


n, m = map(int, sys.stdin.readline().split())

tree_list = list(map(int, sys.stdin.readline().split()))
print(find_cut_height(0,max(tree_list),m))

