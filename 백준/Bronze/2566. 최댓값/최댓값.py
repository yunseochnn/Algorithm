import sys
input = sys.stdin.readline
arr = [list(map(int,input().split())) for _ in range(9)]
loc = []
max_value = -float('inf')
for row in range(9):
    for val in range(9):
        if arr[row][val] > max_value:
            max_value = arr[row][val]
            loc = [row+1,val+1]
print(max_value)
print(loc[0],loc[1])