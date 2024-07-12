from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
dp, idx, result = [], [], []

for i in arr:
    cur = bisect_left(dp,i)
    if cur >= len(dp):
        dp.append(i)
    else:
        dp[cur] = i
    idx.append(cur)

max_value = max(idx)
for i in range(n-1,-1,-1):
    if idx[i] == max_value:
        result.append(arr[i])
        max_value -= 1
print(len(result))
print(*result[::-1])