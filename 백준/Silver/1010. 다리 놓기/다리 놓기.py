import sys
input = sys.stdin.readline

def dp(n, m):
  dp = [[0 for _ in range(m+1)] for _ in range(n+1)] 
  
  for i in range(1, m+1): 
    dp[1][i] = i 
  for i in range(2, n+1): 
    for j in range(i, m+1):
      for k in range(i, j+1):
        dp[i][j] += dp[i-1][k-1]

  return dp[n][m]

T = int(input())
for _ in range(T):
  N, M = map(int, input().split())
  print(dp(N,M))