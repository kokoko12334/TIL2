
t = int(input())
for i in range(t):
    lst = [int(i) for i in input().split()]
    

    summ  = sum(lst[1:])
    aver = summ/lst[0]

    lst2 = [i for i in lst[1:] if i>aver]

    result = len(lst2)/len(lst[1:])*100
    result2 = '{:,.3f}'.format(result) 
    print(f'{result2}%')














