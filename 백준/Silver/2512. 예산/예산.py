import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
m = int(input())

start = 1
end = max(arr)
while start<=end:
    total = 0
    mid = (start+end)//2
    for i in arr:
        if i > mid:
            total += mid
        else:
            total += i
    if total <= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)