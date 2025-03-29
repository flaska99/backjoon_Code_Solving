import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
##크루스칼 알고리즘 : find + union


def find(parent, x) :
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    
    return parent[x]

def union(parnet, a, b) : ## 핵심은 스패닝트리는 어짜피 다 이어져있음
    a_root = find(parent, a)
    b_root = find(parent, b)

    if a_root != b_root:
        parent[b_root] = a_root
        return True
    return False

V, E = map(int, input().split())
edges = []

for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()  # 비용 기준 정렬
parent = [i for i in range(V + 1)]
total = 0

for cost, a, b in edges:
    if union(parent, a, b):
        total += cost

print(total)