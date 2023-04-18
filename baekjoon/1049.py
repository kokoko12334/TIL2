

n,m = [int(i) for i in input().split()]


lst = []
for _ in range(m):
    a,b = [int(i) for i in input().split()]
    lst.append([a,b])


lst_six = sorted(lst, key= lambda x: x[0])
lst_one = sorted(lst, key= lambda x: x[1])

if lst_six[0][0] < lst_one[0][1]*6:
    answer = 0
    while n >= 6:
        answer += lst_six[0][0]
        n-=6


    if n > 0:
        answer += min(lst_six[0][0], lst_one[0][1]*n)


    print(answer)
else:
    print(lst_one[0][1]*n)

