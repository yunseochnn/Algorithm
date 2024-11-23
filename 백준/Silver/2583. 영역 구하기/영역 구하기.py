import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m,n,k = map(int,input().split())
graph = [[0]*n for _ in range(m)]
result = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    global count
    graph[x][y] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<m and 0<=ny<n:
            if graph[nx][ny] == 0:
                count += 1
                graph[nx][ny] = 1
                dfs(nx,ny)

for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = 1
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            count = 1
            dfs(i,j)
            result.append(count)
result.sort()
print(len(result))
print(*result)