n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = list(map(int,input().split()))
    graph[x].append(y)
    graph[y].append(x)
visited = [False for _ in range(n+1)]

def dfs(start):
    visited[start]=True
    count=1
    for i in graph[start]:
        if not visited[i]:
            count+=dfs(i)
    return count
print(dfs(1)-1)