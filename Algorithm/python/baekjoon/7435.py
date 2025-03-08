from collections import defaultdict

n = int(input())

a = []
b = []
c = []
d = []

for _ in range(n):
    arr = [int(i) for i in input().split()]
    a.append(arr[0])
    b.append(arr[1])
    c.append(arr[2])
    d.append(arr[3])

ab = []
cd = []
for i in range(n):
    for j in range(n):
        ab.append(a[i] + b[j])
        cd.append(c[i] + d[j])

nums_map = defaultdict(int)
for i in range(n * n):
    nums_map[cd[i]] += 1

answer = 0
for i in range(n * n):
    num = ab[i]
    answer += nums_map[-num]

print(answer)