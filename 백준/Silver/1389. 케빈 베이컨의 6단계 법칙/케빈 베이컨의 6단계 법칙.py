n,m = map(int,input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0
for _ in range(m):
    x,y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
min_val = INF
idx = 0
for i in range(1,n+1):
    result = sum(graph[i][1:])
    if min_val > result:
        min_val = result
        idx = i
print(idx)