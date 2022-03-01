
n = int(input())

lst=[list(map(int, input().split())) for _ in range(n)]


for i in range(len(lst)):
    rank = 1
    for j in range(len(lst)):
        if i == j:
            continue
        # if lst[i][1] > lst[j][1] and lst[i][0] > lst[j][0]:
        #     pass
        elif lst[i][1] < lst[j][1] and lst[i][0] < lst[j][0]:
            rank += 1
        # else: pass

    print(rank, end = ' ')


######pass로 된 것은 지워도 됨.






















