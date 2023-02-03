import sys
num = int(sys.stdin.readline())

def cal(num):
    lst = []
    if num%3 == 0:
        a = num/3
        lst.append(a)
    if num%2 == 0:
        b = num/2
        lst.append(b)
    c = num-1
    lst.append(c)
    return lst

dp = {}

lst = [num]

level = 0
while min(lst) > 1:
    
    lst2 = []
    for i in lst:
        new = cal(i)
        dp[i] = new
        lst2 += new
    level += 1
    lst = set(lst2)
    if 1 in lst:
        
        break


print(level)        












