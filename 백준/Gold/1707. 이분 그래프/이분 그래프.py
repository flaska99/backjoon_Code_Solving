import sys
sys.setrecursionlimit(10**6)

def is_bipartite(v, graph, colors):
    for u in graph[v]:
        if colors[u] == 0: # 아직 색칠 x
            colors[u] = -colors[v] # 반대 색으로 색칠
            if not is_bipartite(u, graph, colors):
                return False
            
        elif colors[u] == colors[v]: # 인접노드와 같은 색이라면 이분그래프 x
            return False
    return True


input = sys.stdin.readline

t = int(input())



for _ in range(t):
    v, e = map(int, input().split()) # v는 정점개수, e는 간선개수
    graph = [[] for _ in range(v+1)]
    mod = False
    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    
    color = [0] * (v+1)
    is_bip = True


    for i in range(1, v+1):
        if color[i] == 0:
            color[i] = 1
            if not is_bipartite(i, graph, color):
                is_bip = False
                break

    print("YES" if is_bip else "NO")




