import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n = int(input().strip())
graph=[]
visited = [[0]*n for _ in range(n)]
result = [0,0]
for _ in range(n):
    graph.append(list(input()))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny]:
                if graph[x][y] == graph[nx][ny]:
                    dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            result[0]+=1
for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            result[1]+=1
print(*result)