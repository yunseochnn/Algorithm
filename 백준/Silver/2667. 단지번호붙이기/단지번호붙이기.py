from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    count = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny<0 or ny>=n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
                count+=1
    return count
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

arr = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            arr.append(bfs(i,j))
arr.sort()
print(len(arr))
for i in arr:
    print(i)