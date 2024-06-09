from collections import deque
def solution(people, limit):
    count = 0
    people=deque(sorted(people))
    while people :
        person = people.pop()
        if len(people)>0 and person+people[0]<=limit:
            people.popleft()
        count+=1
    return count