t = int(input())
for _ in range(t):
    n = int(input())
    days = list(map(int,input().split()))
    profit = 0
    max_value = 0
    for i in range(n-1,-1,-1):
        if days[i] > max_value:
            max_value = days[i]
        else:
            profit += max_value-days[i]    
    print(profit)