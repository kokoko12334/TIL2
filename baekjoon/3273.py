n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
target = int(input())
print(arr)
l = 0
r = n - 1
cnt = 0

while l < r:
    s = arr[l] + arr[r]
    if s == target:
        cnt += 1
        l += 1
    elif s < target:
        l += 1
    else:
        r -= 1


print(cnt)