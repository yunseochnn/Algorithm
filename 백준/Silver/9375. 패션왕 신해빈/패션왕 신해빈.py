n = int(input())
for _ in range(n):
    d = {}
    t = int(input())
    for _ in range(t):
        c = input().split()
        if c[1] in d:
            d[c[1]].append(c[0])
        else:
            d[c[1]] = [c[0]]
    cnt = 1
    for i in d:
        cnt *= (len(d[i])+1)
    print(cnt-1)