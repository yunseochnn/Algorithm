import sys
input = sys.stdin.readline
INF = int(1e9)

def solution(n, s, a, b, fares):
    graph = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        graph[i][i] = 0

    for fare in fares:
        i, j, k = fare
        graph[i][j] = k
        graph[j][i] = k
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    arr = []
    for i in range(1, n+1):
        cost = graph[s][i] + graph[i][a] + graph[i][b] # 노드 i를 거쳐가는 비용
        arr.append(cost)
    
    return min(arr)