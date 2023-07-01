import sys

input = sys.stdin.readline

r,c,m = [int(i) for i in input().split()]

lst = [[0]*c for _ in range(r)]

sh = {}
for _ in range(m):
    rr,cc,s,d,z = [int(i) for i in input().split()]
    lst[rr-1][cc-1] = z
    sh[z] = [rr-1,cc-1,s,d,z]

def move(i,rr,cc,s,d,z):
    
    if d == 1:
        stand = r
        go = rr
        res = go
        if s <= res:
            go = go - s
            remov = min(lst2[go][cc], i)
            lst2[go][cc] = max(lst2[go][cc], i)
            if remov:
                removes.append(remov)
        else:
            go = go - res
            s2 = s- res
            iterr = s2//(stand-1) 
            res = s2%(stand-1)
            if iterr%2 == 0:
                go = go + res
                if res:
                    d = 2
            
            else:
                go = stand-1-res
                if not res:
                    d = 2
            remov = min(lst2[go][cc], i)
            lst2[go][cc] = max(lst2[go][cc], i)
            if remov:
                removes.append(remov)
        sh[i] = [go,cc,s,d,z]
        return
    
    elif d == 2:
        stand = r
        go = rr
        res = stand - (go + 1)
        if s <= res:
            go = go + s
            remov = min(lst2[go][cc], i)
            lst2[go][cc] = max(lst2[go][cc], i)
            if remov:
                removes.append(remov)
        else:
            go = go + res
            s2 = s - res
            iterr = s2//(stand-1)
            res = s2 % (stand-1)
            if iterr % 2 == 0:
                go = go - res
                if res:
                    d = 1
            else:
                go = res
                if not res:
                    d = 1
            remov = min(lst2[go][cc], i)
            lst2[go][cc] = max(lst2[go][cc], i)
            if remov:
                removes.append(remov)
        sh[i] = [go, cc, s, d, z]
        return
    

    elif d == 3:
        stand = c
        go = cc
        res = stand - (go + 1)
        if s <= res:
            go = go + s
            remov = min(lst2[rr][go], i)
            lst2[rr][go] = max(lst2[rr][go], i)
            if remov:
                removes.append(remov)
        else:
            go = go + res
            s2 = s - res
            iterr = s2//(stand-1)
            res = s2 % (stand-1)
            if iterr % 2 == 0:
                go = go - res
                if res:
                    d = 4
            else:
                go = res
                if not res:
                    d = 4
            remov = min(lst2[rr][go], i)
            lst2[rr][go] = max(lst2[rr][go], i)
            if remov:
                removes.append(remov)
        sh[i] = [rr, go, s, d, z]
        return

    if d == 4:
        stand = c
        go = cc
        res = go
        if s <= res:
            go = go - s
            remov = min(lst2[rr][go], i)
            lst2[rr][go] = max(lst2[rr][go], i)
            if remov:
                removes.append(remov)
        else:
            go = go - res
            s2 = s - res
            iterr = s2//(stand-1)
            res = s2 % (stand-1)
            if iterr % 2 == 0:
                go = go + res
                if res:
                    d = 3
            else:
                go = stand-1-res
                if not res:
                    d = 3
            remov = min(lst2[rr][go], i)
            lst2[rr][go] = max(lst2[rr][go], i)
            if remov:
                removes.append(remov)
        sh[i] = [rr, go, s, d, z]
        return

#이동하고 잡고, 상어 움직이고 잡아먹고
answer = 0
for i in range(c):
    for j in range(r):
        if lst[j][i]:
            shark = lst[j][i]
            answer += shark
            sh.pop(shark)
            lst[j][i] = 0
            break
    lst2 = [[0]*c for _ in range(r)]
    removes = []
    for k,v in sh.items():
        move(k,*v)
    lst = lst2
    if removes:
        for rem in removes:
            sh.pop(rem)

print(answer)