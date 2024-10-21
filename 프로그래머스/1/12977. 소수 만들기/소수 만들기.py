from itertools import combinations
def solution(nums):
    answer = 0
    c = list(combinations(nums,3))
    for i in c:
        s = sum(i)
        for j in range(2,int(s**0.5)+1):
            if s%j == 0:
                answer += 1
                break
    return len(c)-answer