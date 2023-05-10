import sys
input = sys.stdin.readline

n = int(input())


lst = [[int(i) for i in input().split()]for _ in range(n)]

w = 0
b = 0
def recur(x,y,n):
    global w,b
    color = lst[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if lst[i][j] != color:
                div = n//2
                recur(x,y,div)
                recur(x,y+div,div)
                recur(x+div,y,div)
                recur(x+div,y+div,div)
                return
    if color == 0:
        w += 1
    else:
        b += 1
    

recur(0,0,n)
print(w)
print(b)