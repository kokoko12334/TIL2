from bisect import bisect_left,bisect_right
import sys

input = sys.stdin.readline
n = int(input())

arr = [int(i) for i in input().split()]


lis = [arr[0]]


for i in range(1,len(arr)):

    if lis[-1] < arr[i]:
        lis.append(arr[i])
    
    else:
        idx = bisect_left(lis,arr[i])
        
        lis[idx] = arr[i]


print(len(lis))




