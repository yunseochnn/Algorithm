def solution(k, score):
    arr = []
    answer = []
    for i in score:
        arr.append(i)
        if len(arr)>k:
            arr.remove(min(arr))
        answer.append(min(arr))
    return answer