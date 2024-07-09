import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
start = 0
end = max(arr)

while start<=end:
    sum = 0
    mid = (start+end)//2
    for i in arr:
        if i > mid:
            sum += i - mid
    if sum >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)