
C = int(input())

for i in range(C):
    lst = list(map(int, input().split()))
    num = lst.pop(0)

    average = sum(lst)/num

    cnt = 0
    for i in lst:
        if i > average:
            cnt +=1

    result = round(cnt/num*100, 3)
    result2 = '{:,.3f}'.format(result)
    print(f'{result2}%')









