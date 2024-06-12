t = int(input())
t = 1000-t 
answer = 0
a = [500,100,50,10,5,1]
for i in a:
    if t>=i:
        answer += t//i
        t%=i  
print(answer)