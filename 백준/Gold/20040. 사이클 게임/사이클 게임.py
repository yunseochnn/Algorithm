import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int,input().split())
parent = [0]*n
cycle = False
for i in range(n):
    parent[i] = i
for i in range(m):
    a, b = map(int,input().split())
    if find_parent(parent,a) == find_parent(parent,b):
        cycle=True
        count = i
        break
    else:
        union(parent,a,b)
if cycle:
    print(count+1)
else:
    print(0)