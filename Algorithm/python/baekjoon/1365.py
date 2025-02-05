from bisect import bisect_left
n = int(input())

arr = [int(i) for i in input().split()]

lcs = [arr[0]]

for i in range(1, n):
    
    if lcs[-1] < arr[i]:
        lcs.append(arr[i])

    else:
        idx = bisect_left(lcs, arr[i])
        lcs[idx] = arr[i]


print(n - len(lcs))