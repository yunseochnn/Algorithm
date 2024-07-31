from collections import deque
def bfs(start):
    visited = [False for _ in range(n+1)]
    num = [0]*(n+1)
    q = deque([start])
    visited[start] = True
    while q:
        t = q.popleft()
        for i in graph[t]:
            if not visited[i]:
                num[i] = num[t]+1
                q.append(i)
                visited[i] = True
    return sum(num)
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
result = []
for i in range(1,n+1):
    result.append(bfs(i))
print(result.index(min(result))+1)