import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = dict()
for _ in range(n + m):
    p, f, c = input().split()
    if p not in dic:
        dic[p] = []
    if c == "1" and f not in dic:
        dic[f] = []
    dic[p].append(f)

def file(start, num, file_arr):
    stack = [start]
    while stack:
        cur = stack.pop()  
        for i in dic.get(cur, []):
            if i in dic:  
                stack.append(i)
            else:  
                file_arr.add(i)
                num += 1
    return num

q = int(input())
for _ in range(q):
    file_arr = set()
    num = 0
    path = list(input().strip().split('/'))
    num = file(path[-1], num, file_arr)
    print(len(file_arr), num)
