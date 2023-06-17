from itertools import combinations
import sys
input = sys.stdin.readline

l,c = [int(i) for i in input().split()]
al = input().split()
answer = []
for i in combinations(al, l):
    vol = 0
    con = 0
    for j in i:
        if j in {"a","e","i","o","u"}:
            vol += 1
        else:
            con += 1
    if vol <= 0 or con <= 1:
        continue
    
    answer.append("".join(sorted(i)))

for i in sorted(answer):
    print(i)