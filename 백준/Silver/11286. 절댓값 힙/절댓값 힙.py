import sys, heapq
input = sys.stdin.readline
h = []
n = int(input())
for _ in range(n):
    a = int(input())
    if a != 0:
        heapq.heappush(h,(abs(a),a))
    else:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)