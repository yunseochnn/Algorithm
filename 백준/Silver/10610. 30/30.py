n = input()
n = sorted(n,reverse=True)
s = 0
if '0' not in n:
    print(-1)
else:
    for i in n:
        s += int(i)
    if s % 3 != 0:
        print(-1)
    else:
        print(''.join(n))