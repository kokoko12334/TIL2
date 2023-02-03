x = 10
y = 40
n = 5

def cal(x,n):
    return [x+n, 2*x, 3*x]


dic = {}
answer = 0
lst = [x]
result = False
while min(lst) < y:
    result = True
    lst2 = []
    for i in lst:
        if i in dic.keys():
            pass
        else:
            dic[i] = cal(i,n)
            lst2 += dic[i]
    lst = lst2        
    answer += 1
    if y in set(lst):
        result = False
        break
if result:
    answer = -1

answer


x = 10
y = 40
n = 5


def solution(x, y, n):
    dp = [float('inf')]*(y+1)
    dp[x] = 0
    for i in range(x, y+1):
        if dp[i] == float('inf'):
            continue
        if i+n<=y:
            dp[i+n] = min(dp[i+n], dp[i]+1)
        if i*2<=y:
            dp[i*2] = min(dp[i*2], dp[i]+1)
        if i*3<=y:
            dp[i*3] = min(dp[i*3], dp[i]+1)

    if dp[y]==float('inf'):
        return -1
    else:
        return dp[y]



solution(x,y,n)