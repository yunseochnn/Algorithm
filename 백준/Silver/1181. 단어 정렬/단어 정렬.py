n = int(input())
arr = []
for _ in range(n):
    a = input()
    b = len(a)
    arr.append((a,b))
arr = list(set(arr))
arr.sort(key=lambda x:(x[1],x[0]))
for i in arr:
    print(i[0])