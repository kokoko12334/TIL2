
a,b,c= map(int, input().split())

lst = [a,b,c]

lst2 = []
for i in lst:
    lst2.append(lst.count(i))



if max(lst2) ==3:
    num = lst[lst2.index(max(lst2))]
    print(10000+(num*1000))


elif max(lst2) ==2:
    num = lst[lst2.index(max(lst2))]
    print(1000+(num*100))


else: 
    num = max(lst)
    print(num*100)









