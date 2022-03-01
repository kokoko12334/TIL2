a = input()

b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lst = list(b)
a_upper = a.upper()

ko = []
for i in lst:

   ko.append(a_upper.count(i))

check = [i for i in ko if i != 0]

for i in check:
    if check.count(max(check)) !=1:
        print('?')
        break
    else:
        dic = dict(zip(ko,lst))
        r= dic[max(ko)]
        print(r)
        break


