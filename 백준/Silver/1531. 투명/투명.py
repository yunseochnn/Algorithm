n,m = map(int,input().split())
a = [[0]*100 for _ in range(100)]
cnt = 0
for _ in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            a[i-1][j-1] += 1
for i in range(100):
    for j in range(100):
        if a[i][j] > m:
            cnt += 1
print(cnt)