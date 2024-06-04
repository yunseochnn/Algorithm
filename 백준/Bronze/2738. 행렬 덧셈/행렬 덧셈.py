import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr1 = [list(map(int,input().split())) for _ in range(n)]
arr2 = [list(map(int,input().split())) for _ in range(n)]

for a1,a2 in zip(arr1,arr2):
    for v1,v2 in zip(a1,a2):
        print(v1+v2,end=' ')
    print()