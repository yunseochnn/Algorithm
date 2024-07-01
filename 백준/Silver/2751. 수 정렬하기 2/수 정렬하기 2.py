import sys
input=sys.stdin.readline
n = int(input())
arr=[]
for i in range(n):
    a = int(input())
    arr.append(a)
arr.sort()
for i in arr:
    print(i)