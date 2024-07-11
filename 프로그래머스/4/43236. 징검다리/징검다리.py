def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    start = 1
    end = distance
    result = 0
    while start<=end:
        current = 0
        count = 0
        mid = (start+end)//2
        for rock in rocks:
            if rock >= current + mid:
                current = rock
                count += 1
        if count >= len(rocks)-n:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result