import sys
input = sys.stdin.readline

n = int(input())
s = set()
for _ in range(n):
    command = input().split()
    if len(command) == 1:
        if command[0] == "all":
            s = set(list(range(1,21)))
        else:
            s = set()
    else:
        com,num = command[0],command[1]
        num = int(num)
        if com == "add":
            s.add(num)
        elif com == "remove":
            s.discard(num)
        elif com == "check":
            print(1 if num in s else 0)
        elif com == "toggle":
            if num in s:
                s.discard(num)
            else:
                s.add(num)