
 

def recur(lst, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(lst)):
        next = lst
        num = lst[i]

        for j in recur(next, n-1):
            result.append([num]+j)
    return result

lst = [1,2,3,4]

recur(lst, 2)





for i in range(len(lst)):
    for j in range(len(lst)):
        for k in range(len(lst)):
            print(lst[i], lst[j], lst[k])






def func(a,b):
    n = a+b
    return 2*n

func(1,2)





lst = [1,2,3,4,5]


lst_str = [str(i) for i in lst]




