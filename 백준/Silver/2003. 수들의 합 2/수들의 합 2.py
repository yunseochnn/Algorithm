n, m = map(int,input().split())
arr = list(map(int,input().split()))

end = 0
sum = 0
count = 0
for start in range(n):
    while sum < m and end < n:
        sum += arr[end]
        end += 1
    if sum == m:
        count += 1
    sum -= arr[start]
print(count)