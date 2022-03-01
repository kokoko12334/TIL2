#n, m = list(map(int, input().split()))

n, m = [int(i) for i in input().split()]

n_name = [input() for _ in range(n)]
m_name = [input() for _ in range(m)]

name = {}

for i in m_name:
    if i in name:
        name[i] +=1
    else:
        name[i] = 1

for i in n_name:
    if i in name:
        name[i] +=1
    else:
        name[i] = 1

lst = [k for k, cnt in name.items() if cnt>1]
lst.sort()  #사전순으로 출력
print(len(lst), *lst, sep = '\n')

#################집합으로 풀기

n, m = [int(i) for i in input().split()]

n_set = set([input() for _ in range(n)])
m_set = set([input() for _ in range(m)])

inter = list(m_set & n_set)
inter.sort()
print(len(inter), *inter, sep = '\n')





