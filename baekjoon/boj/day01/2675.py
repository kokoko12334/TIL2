t = int(input())

for i in range(t):
    n, s = input().split()
    n = int(n)
    start = ''
    for j in s:
        start += j*n
    print(start)
