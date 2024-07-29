book = dict()
n = int(input())
for _ in range(n):
    name = input()
    if name in book:
        book[name] += 1
    else:
        book[name] = 1
max_val = max(book.values())
result = []
for n,v in book.items():
    if v == max_val:
        result.append(n)
result.sort()
print(result[0])