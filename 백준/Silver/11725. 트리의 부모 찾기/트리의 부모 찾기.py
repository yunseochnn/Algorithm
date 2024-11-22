from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]

for _ in range(n-1):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(start):
    for i in graph[start]:
        if not result[i]:
            result[i]=start
            dfs(i)
dfs(1)
for i in result[2:]:
    print(i)