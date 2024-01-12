from bisect import bisect_left,bisect_right

# import sys

# input = sys.stdin.readline

n = int(input())

arr = [int(i) for i in input().split()]


lis = [arr[0]]

arr2 = [(0,arr[0])]

for i in range(1,len(arr)):

    if lis[-1] < arr[i]:
        lis.append(arr[i])
        arr2.append((len(lis)-1,arr[i]))
    else:
        idx = bisect_left(lis,arr[i])
        
        lis[idx] = arr[i]
        arr2.append((idx,arr[i]))
    print(lis,arr[i])

# print(len(lis))

print(arr2)

index = len(lis) - 1
stack = []
for e in arr2[::-1]:
    if e[0] == index:
        
        print(e[1])
        index -=1



