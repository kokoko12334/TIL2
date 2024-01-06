
t = int(input())


def dp(n,arr):
    answer = 0
    while len(arr) > 1:
        arr.sort()
        result = arr[0] + arr[1]
        answer += result
        arr = arr[2:]
        arr.append(result)

    return answer



for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(dp(n,arr))

