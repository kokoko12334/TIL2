num = int(input())

test3 = round(num/3)

test5 = round(num/5)


lst = []
for i in range(test3+1):
    for j in range(test5+1):
        if 3*i+5*j ==num:
            lst.append(i+j)
if len(lst) !=0:
    print(min(lst))
else:
    print(-1)

