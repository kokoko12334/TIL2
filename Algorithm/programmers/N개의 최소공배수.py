def gcd(a, b):
    p = a%b
    if p == 0:
        return b
    else:
        return gcd(b, p)

def solution(arr):
    answer = 1
    for n in arr:
        answer = answer*n // gcd(answer, n)
        print(answer)
    return answer