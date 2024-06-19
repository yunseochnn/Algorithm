a = int(input())
arr = list(map(int,input().split()))
dp = [1 for _ in range(a)]
for i in range(1,a):
    for j in range(i):
        if arr[i]<arr[j]:
            dp[i]=max(dp[j]+1,dp[i])
print(max(dp))