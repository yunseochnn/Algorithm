n = int(input())
a = 0
for i in range(1,n+1):
    arr = list(map(int,str(i)))
    if i < 100:
        a+=1
    elif arr[0]-arr[1] == arr[1]-arr[2]:
        a+=1
print(a)