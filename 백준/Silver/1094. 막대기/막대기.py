arr = [64,32,16,8,4,2,1]
n = int(input())
count = 0
for i in range(len(arr)):
    if n >= arr[i]:
        count += 1
        n -= arr[i]
    if n == 0:
        break
print(count)