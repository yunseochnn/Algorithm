import sys
input = sys.stdin.readline
k,n = map(int,input().split())
arr=[]
for _ in range(k):
    arr.append(int(input()))
start = 1
end = max(arr)
while start<=end:
    count = 0
    mid = (start+end)//2
    for i in arr:
        count += i//mid
    if count >= n:
        start = mid+1
    else:
        end = mid - 1
print(end)