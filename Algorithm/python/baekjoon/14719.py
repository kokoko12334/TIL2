import sys

h, w = [int(i) for i in sys.stdin.readline().split()]

wall = [int(i) for i in sys.stdin.readline().split()]

lst = [[0]*w for _ in range(h)]

for i in range(w):
    for j in range(wall[i]):
        idx = h-1-j
        lst[idx][i] = 1



answer = 0
for i in range(h):
    check = lst[i]
    box = []
    for j in check:
        if not box and j == 1:
            box.append(j)
        elif box and j == 0:
            box.append(j)
        elif box and j == 1 and box[-1] == 0:
            answer += box.count(0)
            box = [1]
        elif box and j ==1 and box[-1] == 1:
            box = [1]
               
print(answer)

