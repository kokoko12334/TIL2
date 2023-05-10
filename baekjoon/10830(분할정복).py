import sys
input = sys.stdin.readline
n = int(input())
lst = [input() for _ in range(n)]

def recur(y,x,n):
    c = lst[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if lst[i][j] != c:
                d = n//2
                w1 = recur(y,x,d)
                w2 = recur(y,x+d,d)
                w3 = recur(y+d,x,d)
                w4 = recur(y+d,x+d,d)
                return "("+w1+w2+w3+w4+")"
    if c == "0":
        return "0"
    else:
        return "1"

answer = recur(0,0,n)
print(answer)