n = int(input())
count = 0
total = 0
while True:
    count += 1
    total += count
    if total>n:
        break
print(count-1)