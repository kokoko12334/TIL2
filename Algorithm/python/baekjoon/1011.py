t = int(input())


def check(mid, x, y):
    
    if mid == 1:
        return x + 1 == y
    
    if mid == 2:
        return x + 2 >= y
    

    num = mid - 3
    result = 0
    if (num % 2) == 0:
        num2 = mid // 2
        result = (mid - num2)**2
    else:
        num2 = (mid - 1) // 2
        stand = mid - 1 - num2
        result = ((stand)**2) + stand
    
    return x + result >= y

def cal(x, y):
    l = 0
    r = y - x

    answer = r
    while l < r:
        mid = (l + r) // 2
        if check(mid, x, y):
            answer = mid
            r = mid - 1
        else:
            l = mid + 1

    return answer


for _ in range(t):
    x, y = [int(i) for i in input().split()]
    result = cal(x, y)
    print(result)