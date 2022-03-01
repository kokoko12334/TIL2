#언팩킹 방식
def solve(*a):
    r = 0
    for i in a:
        r += i
    return r

solve(1,2,3,4,5,6,7,8,9,10)



#백준식 풀이 a가 리스트임
def solve2(a):   
    ans = 0
    for i in a:
        ans += i
    return ans


solve2([1,2,3,4,5,6,7,8,9,10])




