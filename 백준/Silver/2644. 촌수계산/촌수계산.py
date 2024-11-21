from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
x,y = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    visited = [False for _ in range(n+1)]
    q = deque([start])
    visited[start] = True
    while q:
        a = q.popleft()
        for i in graph[a]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                result[i] = result[a]+1
bfs(x)
if result[y]!=0:
    print(result[y])
else:
    print(-1)