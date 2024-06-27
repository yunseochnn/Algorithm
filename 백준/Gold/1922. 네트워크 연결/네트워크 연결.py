import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())
result = 0
parent = [0]*(n+1)
for i in range(1,n+1):
    parent[i] = i
edges = []
for _ in range(m):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))
edges.sort()

for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a)!=find_parent(parent,b):
        result+=cost
        union(parent,a,b)
print(result)