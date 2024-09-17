from collections import deque
import sys
input = sys.stdin.readline

m,n,h = map(int,input().split())
graph = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
dx,dy,dz = [-1,1,0,0,0,0],[0,0,-1,1,0,0],[0,0,0,0,-1,1]
day = 0
result = False

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i,j,k))
def bfs():
    while q:
        z,x,y = q.popleft()
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0<=nx<n and 0<=ny<m and 0<=nz<h:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    q.append((nz,nx,ny))
bfs()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                result = True
            else:
                day = max(day,graph[i][j][k])

print(-1 if result == True else day-1)