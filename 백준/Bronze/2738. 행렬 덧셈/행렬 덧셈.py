n, m = map(int,input().split())
arr = []
arr2 = []
for row in range(n):
    a = list(map(int,input().split()))
    arr.append(a)
for row in range(n):
    a = list(map(int,input().split()))
    arr2.append(a)
for row in range(n):
    for col in range(m):
        print(arr[row][col]+arr2[row][col], end=' ')
    print()