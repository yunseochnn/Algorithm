from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]

q = deque([(0,0)])
dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx and nx<n and 0<=ny and ny<m:
            if graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y]+1
print(graph[n-1][m-1])