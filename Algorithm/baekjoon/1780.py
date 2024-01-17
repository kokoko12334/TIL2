import sys
input = sys.stdin.readline

n = int(input())

lst = [[int(i) for i in input().split()]for _ in range(n)]

zero = 0
one = 0
minus = 0
def recur(y,x,n):
    global zero,one,minus
    c = lst[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if lst[i][j] != c:
                d = n//3

                for k in [0,1,2]:
                    for u in [0,1,2]:
                        recur(y+d*k, x+d*u,d)
                return
    if c == 0:
        zero += 1
    elif c == 1:
        one += 1
    else:
        minus += 1

recur(0,0,n)
print(minus)
print(zero)
print(one)