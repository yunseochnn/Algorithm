import sys
input = sys.stdin.readline
n,c = map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort()

start = 1
end = arr[-1] - arr[0]
while start<=end:
    current = arr[0]
    count = 1
    mid = (start+end)//2
    for i in range(1,n):
        if arr[i] >= current + mid:
            current = arr[i]
            count+=1
    if count >= c:
        start = mid+1
    else:
        end = mid - 1
print(end)