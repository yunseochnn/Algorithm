import sys
input = sys.stdin.readline
n,m = map(int,input().split())
d = {}
for i in range(1,n+1):
    p = input().rstrip()
    d[i] = p
    d[p] = i
for _ in range(m):
    a = input().rstrip()
    if a.isdigit():
        print(d[int(a)])
    else:
        print(d[a])