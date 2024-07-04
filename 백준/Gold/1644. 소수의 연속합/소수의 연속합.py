import sys, math
input = sys.stdin.readline
n = int(input())
arr = []
a=[1 for _ in range(n+1)]
for i in range(2,int(math.sqrt(n))+1):
    a[i] = i
for i in range(2,n+1):
    if (a[i]==0):
            continue
    for j in range(i+i, n+1, i):
         a[j] = 0
for i in range(2,n+1):
     if a[i] != 0:
          arr.append(i)
start = 0
end = 0
sum = 0
count = 0

for start in range(len(arr)):
    while end < len(arr) and sum < n:
        sum += arr[end]
        end += 1
    if sum == n:
        count += 1
    sum -= arr[start]
print(count)