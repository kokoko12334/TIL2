
n = int(input())
lst = [input() for _ in range(n)]


dic = {}
for i in lst:
    for j in i:
        dic[j] = 0

# 알파벳이 포함된 자릿수를 구한다.
for i in lst:
    digits= len(i) - 1
    for j in i:
        dic[j] += 10**(digits)
        digits -= 1

sor_values = sorted(dic.values(), reverse= True)

num = 9
total = 0
for i in sor_values:
    total += num * i
    num -= 1
print(total)