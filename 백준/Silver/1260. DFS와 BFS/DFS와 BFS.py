from collections import deque
n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = list(map(int,input().split()))
    graph[x].append(y)
    graph[y].append(x)
for i in graph:
    i.sort()
def dfs(start):
    visited[start] = True
    print(start,end=" ")
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        t = q.popleft()
        print(t, end=" ")
        for i in graph[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
visited = [False for _ in range(n+1)]
dfs(v)
print()
visited = [False for _ in range(n+1)]
bfs(v)