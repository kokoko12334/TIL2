t = int(input())
lst = [int(i) for i in input().split()]
cnt = 0

for i in lst:
    if i ==1:
        continue
    if i in [2,3,5,7]:
        cnt += 1
    elif i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0:
        cnt += 1
    
print(cnt)



# lst = [1,2,3]

# lst.



def prime(n):
    if n==1:
        return -1
    else:    
        lst = [i for i in range(1,n+1) if i%2 != 0 ]

        lst[0] = 2
        if len(lst)>6:
            result = lst[:4]
            for i in lst[5:]:
                if i%3 != 0 and i%5 != 0 and i%7 != 0 :
                    result.append(i)
            return result
        elif len(lst)<6:
            return lst     
        else:
            return lst[:-1]

prime(123)









