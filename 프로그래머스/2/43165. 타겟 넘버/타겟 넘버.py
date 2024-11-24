def solution(numbers, target):
    count = 0
    def dfs(idx,x):
        nonlocal count
        if idx == len(numbers):
            if x == target:
                count += 1
            return
        else:
            dfs(idx+1,x+numbers[idx])
            dfs(idx+1,x-numbers[idx])
    dfs(0,0)
    return count