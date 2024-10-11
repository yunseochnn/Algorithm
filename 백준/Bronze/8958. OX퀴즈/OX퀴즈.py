t = int(input())
for _ in range(t):
    a = input()
    score = 0
    result = 0
    for i in a:
        if i == "O":
            score += 1
        else:
            score = 0
        result += score
    print(result)