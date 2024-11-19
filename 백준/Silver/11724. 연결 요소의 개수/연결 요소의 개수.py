import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
count = 0

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        count += 1
print(count)