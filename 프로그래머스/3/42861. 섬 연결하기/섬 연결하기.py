def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
def solution(n, costs):
    answer = 0
    parent = [0]*n
    for i in range(n):
        parent[i]=i
    arr=[]
    for cost in costs:
        a,b,c = cost
        arr.append((c,a,b))
    arr.sort()
    for i in arr:
        c,a,b = i
        if find_parent(parent,a)!=find_parent(parent,b):
            answer+=c
            union(parent,a,b)
    return answer