n = int(input())
arr = list(map(int,input().split()))
arr.sort()

left = 0
right = n-1

answer = 2e+9+1
arr2 = []
while left<right:
    l = arr[left]
    r = arr[right]
    plus = l+r

    if abs(plus) < answer:
        answer = abs(plus)
        arr2=[l,r]
    if plus < 0:
        left+=1
    else:
        right-=1
print(*arr2)