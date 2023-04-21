
n = int(input())

lst_p = []
lst_n = []

for _ in range(n):
    num = int(input())
    if num > 0:
        lst_p.append(num)
    else:
        lst_n.append(num)

lst_p.sort()
lst_n.sort(reverse=True)

answer = 0
while lst_p:
    n1 = lst_p.pop()
    if lst_p:
        n2 = lst_p.pop()
    else:
        n2 = 0
    answer += max(n1+n2, n1*n2)


while lst_n:
    n1 = lst_n.pop()
    if lst_n:
        n2 = lst_n.pop()
    else:
        n2 = 1
    answer += (n1*n2)


print(answer)



