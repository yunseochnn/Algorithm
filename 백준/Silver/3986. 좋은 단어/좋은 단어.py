n = int(input())
result = 0
for _ in range(n):
    s = []
    l = list(input())
    for i in l:
        if s:
            if i == s[-1]:
                s.pop()
            else:
                s.append(i)
        else:
            s.append(i)
    if not s:
        result += 1
print(result)