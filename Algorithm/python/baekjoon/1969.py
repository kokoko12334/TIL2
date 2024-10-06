import sys
input = sys.stdin.readline

n,m = [int(i) for i in input().split()]


dna = [input() for _ in range(n)]

answer = ""
summ = 0
for i in range(m):
    sett = set()
    dic = {}
    for j in range(n):
        if dna[j][i] not in sett:
            dic[dna[j][i]] = 1
            sett.add(dna[j][i])
        else:
            dic[dna[j][i]] += 1
    maxx = -1
    dic = dict(sorted(dic.items()))
    strr = ""
    total = 0
    for k,v in dic.items():
        total += v
        if v > maxx:
            maxx = v
            strr = k
    answer += strr
    total -= maxx
    summ += total
    
print(answer)
print(summ)

