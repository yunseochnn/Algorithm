n = int(input())
for _ in range(n):
    a = input()
    while a.count("()")!=0:
        a=a.replace("()","")
    if len(a) == 0:
        print("YES")
    else:
        print("NO")
   