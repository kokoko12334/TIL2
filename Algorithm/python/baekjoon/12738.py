from bisect import bisect_left
n = int(input())

arr = [int(i) for i in input().split()]


lcs = [arr[0]]

for i in range(1, n):
    num = arr[i]

    if lcs[-1] < num:
        lcs.append(num)
    else:
        idx = bisect_left(lcs, num)
        lcs[idx] = num

print(len(lcs))