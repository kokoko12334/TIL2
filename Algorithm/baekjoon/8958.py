
a = int(input())

for i in range(a):
    lst = list(input())

    i = 0
    r = 0
    while len(lst) >0:
     if lst[0] =='O':
         r += (i+1)
         lst.remove(lst[0])
         i += 1         #연속된 'O'에 대해서 +1씩 증가하므로
     else:
         lst.remove('X')
         i = 0
    
    print(r)



