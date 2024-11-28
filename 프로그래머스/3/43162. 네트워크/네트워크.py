def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    def dfs(i):
        visited[i] = True
        for j in range(n):
            if j != i and not visited[j]:
                if computers[i][j] == 1:
                    dfs(j)
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer