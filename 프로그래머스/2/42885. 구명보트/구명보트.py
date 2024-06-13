def solution(people, limit):
    people.sort()
    start = 0
    end = len(people)-1
    answer = 0
    while start<=end:
        if people[end]+people[start]<=limit:
            answer+=1
            end-=1
            start+=1
        else:
            answer+=1
            end-=1
    return answer