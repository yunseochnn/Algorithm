c = int(input())
for _ in range(c):
    n = list(map(int,input().split()))
    avg = sum(n[1:])/n[0]
    cnt = 0
    for i in n[1:]:
        if i>avg:
            cnt+=1
    rate = cnt/n[0] * 100
    print(f'{rate:.3f}%')