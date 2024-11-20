import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
max_val = max(map(max,graph))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,h):
    arr[x][y] = True
    for m in range(4):
        nx = x+dx[m]
        ny = y+dy[m]
        if 0<=nx<n and 0<=ny<n and not arr[nx][ny] and graph[nx][ny] > h :
            arr[nx][ny] = True
            dfs(nx,ny,h)
result = 0
for h in range(max_val):
    arr = [[False]*n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not arr[i][j]:
                dfs(i,j,h)
                count += 1
    result = max(result,count)
print(result)