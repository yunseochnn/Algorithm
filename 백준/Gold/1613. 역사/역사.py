import sys
input = sys.stdin.readline

n,k = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(k):
    x,y = map(int,input().split())
    graph[x][y] = 1
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1
s = int(input())
for _ in range(s):
    a, b = map(int,input().split())
    if graph[a][b] == 1:
        print(-1)
    elif graph[b][a] == 1:
        print(1)
    elif graph[a][b] == 0:
        print(0)