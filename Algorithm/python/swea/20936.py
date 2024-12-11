
t = int(input())

def check(n):
    for i in range(1, n + 1):
        if num_to_idx[i] != i - 1:
            return i
    return -1

for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]

    idx_to_num = dict()
    num_to_idx = dict()
    start = -1
    for i in range(n):
        num = arr[i]
        idx_to_num[i] = num
        num_to_idx[num] = i
        if num - 1 != i:
            start = num
    
    start = check(n)
    if start == -1:
        print(0)
        print()
    else:
        cnt = 1
        result = []
        while start != -1:
            x_idx = num_to_idx[start]
            result.append(x_idx + 1)
            num_to_idx[start] = n
            while x_idx != n:
                num = x_idx + 1
                idx = num_to_idx[num]
                num_to_idx[num] = x_idx
                x_idx = idx
                result.append(x_idx + 1)
                cnt += 1
            start = check(n)
        print(cnt)
        print(*result)