from itertools import combinations
lst = [int(input()) for _ in range(9)]


summ = sum(lst)
found = False
for i in range(len(lst)):

    for j in range(i+1, len(lst)):
        a1 = lst[i]
        a2 = lst[j]
        a = a1+a2
        result = summ - a

        if result == 100:

            lst.remove(a1)
            lst.remove(a2)

            lst.sort()
            for k in lst:
                print(k)
            found = True
            break
    if found:
        break
























