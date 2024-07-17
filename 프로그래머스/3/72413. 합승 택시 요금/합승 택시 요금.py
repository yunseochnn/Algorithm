import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)
def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    for i in fares:
        x,y,z = i
        graph[x].append((y,z))
        graph[y].append((x,z))
    def dijkstra(start):
        distance = [INF]*(n+1)
        q = []
        heapq.heappush(q,(0,start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if dist > distance[now]:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost,i[0]))
        return distance
    arr = []
    t1 = dijkstra(s)
    for i in range(1,n+1):
        result = dijkstra(i)
        arr.append(result[a]+result[b]+t1[i])
    return min(arr)
