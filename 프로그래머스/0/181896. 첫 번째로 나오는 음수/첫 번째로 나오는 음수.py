def solution(num_list):
    answer = 0
    for i in num_list:
        if i<0:
            answer = num_list.index(i)
            return answer
    return -1
