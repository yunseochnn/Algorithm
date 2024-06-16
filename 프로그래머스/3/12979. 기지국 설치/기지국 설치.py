from math import ceil
def solution(n, stations, w):
    valid = 2*w+1
    start = 1
    answer = 0

    for st in stations:
        if st-w > start:
            answer += ceil((st-w-start)/valid)
        start = st + w + 1
    if n >= start:
        answer += ceil((n-start+1)/valid)
    return answer