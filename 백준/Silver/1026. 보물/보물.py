n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
answer = 0

for i in range(n):
    max_value = max(b)
    b.remove(max_value)
    answer += a[i]*max_value
print(answer)
