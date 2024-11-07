n = int(input())
d = len(str(n))
result = 0
for i in range(1,d):
    result += 9*10**(i-1)*i
result += (n-10**(d-1)+1)*d
print(result)