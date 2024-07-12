import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr1 = set(map(int,input().split()))
    n2 = int(input())
    arr2 = list(map(int,input().split()))
    for i in arr2:
        if i in arr1:
            print(1)
        else:
            print(0)