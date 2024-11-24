from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append([numbers[0],0])
    q.append([numbers[0]*-1,0])
    while q:
        x,idx = q.popleft()
        idx += 1
        if idx<len(numbers):
            q.append([x+numbers[idx],idx])
            q.append([x-numbers[idx],idx])
        else:
            if x == target:
                answer += 1
    return answer