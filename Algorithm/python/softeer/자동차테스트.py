import sys
from bisect import bisect_left
input = sys.stdin.readline

n, q = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
arr.sort()
arr_n = len(arr)
arr_set = set(arr)
for _ in range(q):
    m = int(input())
    if m not in arr_set:
        print(0)
        continue
    idx = bisect_left(arr, m)
    
    left = idx
    right = arr_n - idx - 1
    print(left * right)
    
        