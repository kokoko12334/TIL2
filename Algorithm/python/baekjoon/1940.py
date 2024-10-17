n = int(input())
m = int(input())

arr = [int(i) for i in input().split()]

arr.sort()

l = 0
r = n - 1
answer = 0

while l < r:
    num = arr[l] + arr[r]
    if num == m:
        answer += 1
    if num <= m:
        l += 1
    else:
        r -= 1

print(answer)