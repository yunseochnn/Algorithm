def cycle(n):
    if len(n)<2:
        n = '0'+n
    origin = n
    count = 0
    while True:
        val = sum(int(digit) for digit in n)
        n = n[-1]+str(val)[-1]
        count += 1
        if n == origin:
            return count
n = input()
print(cycle(n))