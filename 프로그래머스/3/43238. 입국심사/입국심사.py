def solution(n, times):
    start = 1
    end = max(times)*n
    result = 0
    while start<=end:
        count = 0
        mid = (start+end)//2
        for t in times:
            count += (mid//t)
        if count >= n:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result