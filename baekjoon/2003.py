import sys

input = sys.stdin.readline

n,m = [int(i) for i in input().split()]

lst = [int(i) for i in input().split()]

start = 0
end = 0
sum_ = lst[0]
cnt = 0

while True:

    if sum_ == m:
        cnt += 1

    if sum_ <= m:
        end += 1
        if end > n-1:
            break
        sum_ += lst[end]

    else:
        sum_ -= lst[start]
        start += 1
    
print(cnt)






