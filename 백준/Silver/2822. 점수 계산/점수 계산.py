arr=[int(input()) for _ in range(8)]
li = sorted(arr)[3:]
result = []
print(sum(li))
for i in li:
    result.append(arr.index(i)+1)
print(*sorted(result))