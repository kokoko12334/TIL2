
n = int(input())

lst = [[int(i) for i in input().split()] for i in range(n)]

lst2 = [i for i in range(1,n+1)]


level = n//2
#v level 누적
stack = [[1,1,0,[1]]]
answer = 999999999

while stack:
    out = stack.pop()
    v,l,c,t = out[0], out[1],out[2], out[3]

    if l == level:
        c2 = 0
        iter = set(lst2) - set(t)
        for i in iter:
            for j in iter:
                c2 += lst[i-1][j-1]
        result = abs(c - c2)
        if answer > result:
            answer = result
    else:
        for i in range(v,n):
            c_h = c
            next_v = lst2[i]
            for j in t:
                c_h += (lst[next_v-1][j-1] + lst[j-1][next_v-1])

            stack.append([next_v,l+1, c_h,t+[next_v]])


print(answer)





