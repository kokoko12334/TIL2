def solution(sequence):
    answer = 0
    n = len(sequence)
    arr1 = [0]
    for i in range(n):
        if i%2:
            num = sequence[i]
        else:
            num = -sequence[i]
        arr1.append(num)
    arr1 = arr1[1:]
    arr2 = [-i for i in arr1]
    
    answer = 0
    dp1 = [0] * (n+1)
    for i in range(n):
        dp1[i] = max(dp1[i-1] + arr1[i], arr1[i])
    dp2 = [0] * (n+1)
    for i in range(n):
        dp2[i] = max(dp2[i-1] + arr2[i], arr2[i])
    answer = max(max(dp1), max(dp2))
    return answer