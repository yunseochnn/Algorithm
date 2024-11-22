from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for _ in range(n-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
def bfs(start):
    q = deque([start])
    while q:
        a = q.popleft()
        for i in graph[a]:
            if not result[i]:
                result[i] = a
                q.append(i)
bfs(1)
for i in result[2:]:
    print(i)