n = int(input())
for _ in range(n):
    s=[]
    a = input()
    valid = True
    for i in a:
        if i == "(":
            s.append(i)
        elif i == ")":
            if not s:
                valid = False
                break
            else:
                s.pop()
    if valid and not s:
        print("YES")
    else:
        print("NO")