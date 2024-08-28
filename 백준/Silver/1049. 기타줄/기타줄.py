n,m = map(int,input().split())
p = []
s = []
for _ in range(m):
    a,b = map(int,input().split())
    p.append(a)
    s.append(b)
min_p = min(p)
min_s = min(s)
answer = 0
if min_s*6>min_p:
    if min_p<min_s*(n%6):
        answer = min_p*(n//6+1)
    else:
        answer = min_p*(n//6)+min_s*(n%6)
else:
    answer = min_s*n
print(answer)