n = int(input())
t = list(input())
colors = {'B': 0,'R':0}
colors[t[0]] += 1
for i in range(1,n):
    if t[i] != t[i-1]:
        colors[t[i]]+=1
answer = min(colors['B'], colors['R'])+1
print(answer)