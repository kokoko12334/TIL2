import sys
n, k = map(int, sys.stdin.readline().split())

lst = []
for i in range(1, n+1):
    if n % i == 0:
        lst.append(i)

if len(lst) >= k:

    print(lst[k-1])
else:
    print(0)
