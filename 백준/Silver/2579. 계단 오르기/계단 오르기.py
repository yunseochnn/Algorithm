n = int(input())
dp = [0]*(n+1)
arr=[]
for i in range(n):
    arr.append(int(input()))
dp[1] = arr[0]
for i in range(2,len(arr)+1):
    dp[i] = max(dp[i-3]+arr[i-2],dp[i-2])+arr[i-1]
print(dp[n])