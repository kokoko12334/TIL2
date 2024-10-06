def solution(n, s):
    
    num = s//n
    re = s%n
    if num == 0:
        return [-1]
    arr = [num]*(n-re) + [num+1]*(re)
    
    return arr