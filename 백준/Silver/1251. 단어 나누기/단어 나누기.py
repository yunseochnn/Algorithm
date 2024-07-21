text = input()
result = []
for i in range(1,len(text)-1):
    for j in range(i+1,len(text)):
        t1=text[:i][::-1]
        t2=text[i:j][::-1]
        t3=text[j:][::-1]
        result.append(t1+t2+t3)
print(sorted(result)[0])