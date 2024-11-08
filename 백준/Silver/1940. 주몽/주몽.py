n = int(input())
m = int(input())
arr = list(map(int,input().split()))
arr.sort()
left = 0
right = len(arr)-1
count = 0
while left<right:
    s = arr[left]+arr[right]
    if s > m:
        right -= 1
    elif s < m:
        left += 1
    elif s == m:
        count += 1
        left += 1
        right -= 1
print(count)