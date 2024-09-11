import sys
input = sys.stdin.readline
import heapq
n = int(input())
h = []
for _ in range(n):
    a = int(input())
    if a != 0:
        heapq.heappush(h,(-a,a))
    else:
        if len(h)>=1:
            print(heapq.heappop(h)[1])
        else:
            print(0)