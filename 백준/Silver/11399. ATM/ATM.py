n = int(input())
a = list(map(int,input().split()))
a.sort()
answer = 0
f = [a[0]]*n
for i in range(1,n):
    f[i] = f[i-1]+a[i]
print(sum(f))