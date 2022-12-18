import sys
#sys.stdin.readline()


def comb(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1:], n-1):
                result.append([arr[i]]+j)
    return result

lst = []
n,m = map(int, sys.stdin.readline().split())

lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

home_list = {}
chicken_list = {}
cnt1 = 0
cnt2 = 0
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] == 1:
            home_list[cnt1] = [i,j]
            cnt1 +=1
        if lst[i][j] == 2:
            chicken_list[cnt2] = [i,j]
            cnt2 +=1
                

ch_len = len(chicken_list.keys())

lst2 = comb(list(chicken_list.keys()), m)

result_lst = []
for i in range(len(lst2)):
    s = lst2[i]
    result = 0
    for j in home_list.keys():
        dis_lst = []
        for k in s:
            x = home_list[j][0]-chicken_list[k][0]
            y = home_list[j][1]-chicken_list[k][1]
            
            
            dis = abs(x)+abs(y)
                  
            dis_lst.append(dis)
           
        minn = min(dis_lst)
           
        result += minn
    result_lst.append(result)

print(min(result_lst))


