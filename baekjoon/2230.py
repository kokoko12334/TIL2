import sys

input = sys.stdin.readline

n,m = [int(i) for i in input().split()]

lst = []

for _ in range(n):
    num = int(input())
    lst.append(num)

lst.sort()

start = 0
end = 0
min_diff = float("inf")

while True:

    diff = abs(lst[start] - lst[end])

    if diff>= m and min_diff > diff:
        min_diff = diff
    
    if diff == m:
        break

    if diff >= m:
        start += 1
    else:
        end += 1
        if end >= n:
            break

print(min_diff)

