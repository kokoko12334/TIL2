
n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))


lst.sort(reverse= True)

for i in range(n):
    lst[i] = lst[i]*(i+1)

print(max(lst))
