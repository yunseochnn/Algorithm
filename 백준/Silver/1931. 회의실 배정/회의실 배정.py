import sys
input = sys.stdin.readline
n = int(input())
arr=[]
for _ in range(n):
    a, b= map(int,input().split())
    arr.append((a,b))
arr.sort(key=lambda x:(x[1],x[0]))
point = 0
count = 0

for start,end in arr:
    if point <= start:
        count += 1
        point = end
print(count)