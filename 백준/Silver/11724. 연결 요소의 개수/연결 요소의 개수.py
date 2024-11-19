import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
count = 0

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)