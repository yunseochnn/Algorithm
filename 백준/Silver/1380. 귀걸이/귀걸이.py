answer = []
while True:
    n = int(input())
    if n == 0:
        break
    stu = []
    stack = []
    for i in range(n):
        stu.append(input())
    for i in range(2*n-1):
        a = int(input().split()[0])
        if a in stack:
            stack.remove(a)
        else:
            stack.append(a)
    answer.append(stu[stack[0]-1])
for idx,i in enumerate(answer):
    print(idx+1,i)