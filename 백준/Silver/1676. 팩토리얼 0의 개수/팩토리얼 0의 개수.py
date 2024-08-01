n = int(input())
def factorial(n):
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1,n+1):
        dp[i] = dp[i-1]*i
    return dp[n]
result = str(factorial(n))[::-1]
cnt = 0
for i in result:
    if i!='0':
        break
    cnt += 1
print(cnt)