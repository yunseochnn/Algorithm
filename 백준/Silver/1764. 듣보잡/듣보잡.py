n,m = map(int,input().split())
arr1 = set()
arr2 = set()
for _ in range(n):
    arr1.add(input())
for _ in range(m):
    arr2.add(input())
result = sorted(list(arr1&arr2))
print(len(result))
for i in result:
    print(i)