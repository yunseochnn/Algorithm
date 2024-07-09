from bisect import bisect_left, bisect_right
import sys 
input=sys.stdin.readline
def count_by_range(arr,left_value,right_value):
    right_index = bisect_right(arr,right_value)
    left_index = bisect_left(arr,left_value)
    return right_index - left_index

n = int(input())
arr1 = list(map(int,input().split()))
arr1.sort()
m = int(input())
arr2 = list(map(int,input().split()))

for i in arr2:
    print(count_by_range(arr1,i,i),end = ' ')