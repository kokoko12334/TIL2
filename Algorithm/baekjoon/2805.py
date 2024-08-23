import sys
n, m = [int(i) for i in sys.stdin.readline().split()]


lst = [int(i) for i in sys.stdin.readline().split()]

s, e = 0, max(lst)

while s < e:
    mid = (s+e+1)//2
    print(s,e)
    total = 0
    for i in lst: 
        if i > mid:
            total += (i-mid)
    if total >= m:
            s = mid
    else:
        e = mid - 1


print(e)
