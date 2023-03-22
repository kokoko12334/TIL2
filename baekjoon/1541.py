
string = input()

a = string.split("-")

total = 0

f = a[0].split("+")

for i in f:
    total += int(i)


for i in a[1:]:
    b = 0
    c = i.split("+")
    for j in c:
        b += int(j)
    total -= b

print(total)







