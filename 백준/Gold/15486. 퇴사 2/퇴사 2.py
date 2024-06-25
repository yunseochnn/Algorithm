import sys
n= int(sys.stdin.readline())
tasks = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [0] * (n + 1)

for i in range(n):
    time, profit = tasks[i]
    if i + 1 <= n:
        dp[i + 1] = max(dp[i + 1], dp[i])
    if i + time <= n:
        dp[i + time] = max(dp[i + time], dp[i] + profit)
print(max(dp))