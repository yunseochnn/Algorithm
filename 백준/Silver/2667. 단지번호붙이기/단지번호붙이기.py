n = int(input())
graph = [list(map(int,input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

arr = []
count = 0
def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if graph[x][y] == 1:
        global count
        count+=1
        graph[x][y] = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(nx,ny)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            arr.append(count)
            count = 0
arr.sort()
print(len(arr))
for i in arr:
    print(i)