

def dfs(i, total):
    if total > i :
        return 0
    
    if total == i :
        return 1
    
    return dfs(i, total + 1) + dfs(i, total + 2) + dfs(i, total + 3)


t = int(input())

for i in range(t) :
    n = int(input())
    print(dfs(n, 0))