n,m = [int(i) for i in input().split()]

lst = [int(i) for i in input().split()]

case = []
for i in range(len(lst)):
    lst2 = lst.copy()
    s1 = lst[i]
    lst2.pop(i)
    for j in range(len(lst2)):
    
        lst3 = lst2.copy()
        s2 =lst2[j]
        lst3.pop(j)
        for k in range(len(lst3)):
            
            lst4 = lst3.copy()
            s3 = lst3[k]
            case.append([s1, s2, s3])      

lst2 = list(set([sum(i) for i in case if sum(i)<=m]))

if m in lst2:
    print(m)
else:
    lst2.append(m)
    lst2.sort()
    
    print(lst2[-2])
    
