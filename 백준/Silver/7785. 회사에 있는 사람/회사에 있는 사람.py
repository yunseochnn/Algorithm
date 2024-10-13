import sys
input = sys.stdin.readline
n = int(input())
d = dict()
for _ in range(n):
    p, state = input().split()
    if state == "enter":
        d[p] = True
    else:
        del d[p]
print("\n".join(sorted(d.keys(),reverse=True)))