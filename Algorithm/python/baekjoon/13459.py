n, k = [int(i) for i in input().split()]

if n <= k:
    re = k % n
    print(re)
else:
    print(n - k)


