num = int(input())
arr = [list(map(int,input().split())) for _ in range(num)]
result = [[0]*num for _ in range(num)]
for i in range(5):
    for j in range(num):
        for k in range(j+1,num):
            if arr[j][i] == arr[k][i]:
                result[k][j] = 1
                result[j][k] = 1
cnt = []
for i in result:
    cnt.append(i.count(1))
print(cnt.index(max(cnt))+1)