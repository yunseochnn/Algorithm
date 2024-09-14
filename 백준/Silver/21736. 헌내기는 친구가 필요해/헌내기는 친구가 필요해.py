from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            start = (i,j)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0]*m for _ in range(n)]
result = 0

q = deque([start])
visited[start[0]][start[1]] = 1
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny] != "X" and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = 1
                if graph[nx][ny] == "P":
                    result += 1
print(result if result > 0 else "TT")