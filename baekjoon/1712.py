A, B, C = map(int, input().split())
if C <= B:
    print(-1)
else:
    x = int(A/(C-B)+1)
    print(x)

