
paper = [[0]*100 for _ in range(100)]

lst = [list(map(int, input().split())) for _ in range(4)]


for i in range(len(lst)):
    for j in range(lst[i][1],lst[i][3]):
        for k in range(lst[i][0],lst[i][2]):
            paper[j][k] = 1

cnt = 0
for i in range(100):
    cnt += paper[i].count(1)

print(cnt)


############################
paper = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            paper[i][j] = 1

print(sum(sum(line) for line in paper))