def hanoi(num,f,to,other):
    if num == 1:
        print(f,to,end=' ')
        print()
        return
    hanoi(num-1,f,other,to)
    print(f,to,end=' ')
    print()
    hanoi(num-1,other,to,f)

n = int(input())
print(2**n-1)
hanoi(n,1,3,2)