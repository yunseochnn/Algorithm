def solution(brown, yellow):
    a = brown//2 + 2
    b = brown+yellow
    arr = []
    for i in range(1,brown):
        for j in range(i, brown):
            if j+i == a and j*i == b:
                arr.append(j)
                arr.append(i)
    return arr