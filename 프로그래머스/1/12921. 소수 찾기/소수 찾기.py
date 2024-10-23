def solution(n):
    answer = 0
    for i in range(2,n+1):
        isDec = True
        n = int(i**0.5)+1
        for j in range(2,n):
            if i % j == 0:
                isDec = False
                break
        if isDec:
            answer += 1
    return answer