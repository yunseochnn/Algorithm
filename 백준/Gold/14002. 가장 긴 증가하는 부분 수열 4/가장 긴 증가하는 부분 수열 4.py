n = int(input())
arr = list(map(int,input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i] = max(dp[i],dp[j]+1)
a = max(dp)
print(a)
result = []
for i in range(n-1,-1,-1):
    if dp[i] == a:
        result.append(arr[i])
        a -= 1
result.reverse()
for i in result:
    print(i,end=' ')