n = int(input())

arr = [int(i) for i in input().split()]
arr.sort()
answer = 0

for i in range(n):
    l = 0
    r = n - 1
    target = arr[i]
    if l == i:
        l += 1
    elif r == i:
        r -= 1
    while l < r:
        
        num = arr[l] + arr[r]
        if num == target:
            answer += 1
            break

        if num < target:
            l += 1
        else:
            r -= 1

        if l == i:
            l += 1
        elif r == i:
            r -= 1

print(answer)