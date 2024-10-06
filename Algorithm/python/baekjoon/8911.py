import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    commands = list(input())[:-1]

    d = (1,0)
    ny, py, nx, px = 0, 0, 0, 0
    y, x = 0, 0
    for i in range(len(commands)):
        c = commands[i]
        if c == 'F':
            y += d[0]
            x += d[1]

            if y < 0:
                ny = max(abs(y), ny)
            else:
                py = max(y, py)
            if x < 0:
                nx = max(abs(x), nx)
            else:
                px = max(x, px)

        elif c == 'B':
            y -= d[0]
            x -= d[1]
            if y < 0:
                ny = max(abs(y), ny)
            else:
                py = max(y, py)
            if x < 0:
                nx = max(abs(x), nx)
            else:
                px = max(x, px)
        elif c == 'L':
            if d == (1, 0):
                d = (0, -1)
            elif d == (0, -1):
                d = (-1, 0)
            elif d == (0, 1):
                d = (1, 0)
            else:
                d = (0, 1)
        else:
            if d == (1, 0):
                d = (0, 1)
            elif d == (0, -1):
                d = (1, 0)
            elif d == (0, 1):
                d = (-1, 0)
            else:
                d = (0, -1)
    answer = (ny+py) * (nx+px)
    print(answer)


#y,x
#(1,0)  -> l:(0,-1) , r:(0,1)
#(0,-1) -> l:(-1,0) r:(1,0)
#(0,1) -> l:(1,0), r:(-1,0)
# (-1, 0) -> l:(0,1), r:(0,-1)