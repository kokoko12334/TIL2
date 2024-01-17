import sys
n, m = [int(i) for i in sys.stdin.readline().split()]

lst = []
for _ in range(n):
    lst.append([int(i) for i in sys.stdin.readline().split()])

lst2 = []
for _ in range(m):
    lst2.append([int(i) for i in sys.stdin.readline().split()])



dp = [[0]*n]
for i in range(n):
    t = []
    for j in range(n):
        t.append(lst[i][j] + dp[i][j])
    dp.append(t)


for i in lst2:
    x1, y1, x2, y2 = i[0],i[1]-1,i[2],i[3]-1
    
    cum1 = dp[x2]
    cum2 = dp[x1-1]
    
    result = []
    for j in range(y1, y2+1):
        result.append(cum1[j] - cum2[j])
    print(sum(result))
    




