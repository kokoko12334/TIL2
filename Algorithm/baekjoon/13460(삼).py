n,m = map(int, input().split())

lst = []
for _ in range(n):
    lst.append(list(input()))


def left(lst):
    #Red 위치
    for i in range(len(lst)):
        if 'R' in lst[i]:
            s = i

    red_idx = lst[s].index('R')
    #blue 위치
    for i in range(len(lst)):
        if 'B' in lst[i]:
            s_b = i

    blue_idx = lst[s_b].index('B')

    if s == s_b:
        if red_idx < blue_idx:

            while lst[s][red_idx-1] != '#':
                red = lst[s][red_idx]
                pre = lst[s][red_idx-1]
                lst[s][red_idx] = pre
                lst[s][red_idx-1] = red
                red_idx -= 1

            while lst[s_b][blue_idx-1] != '#':
                blue = lst[s_b][blue_idx]
                pre = lst[s_b][blue_idx-1]
                lst[s_b][blue_idx] = pre
                lst[s_b][blue_idx-1] = blue
                blue_idx -= 1
        elif red_idx > blue_idx:

            while lst[s_b][blue_idx-1] != '#':
                blue = lst[s_b][blue_idx]
                pre = lst[s_b][blue_idx-1]
                lst[s_b][blue_idx] = pre
                lst[s_b][blue_idx-1] = blue
                blue_idx -= 1

            while lst[s][red_idx-1] != '#':
                red = lst[s][red_idx]
                pre = lst[s][red_idx-1]
                lst[s][red_idx] = pre
                lst[s][red_idx-1] = red
                red_idx -= 1
    else:
        while lst[s][red_idx-1] != '#':
                red = lst[s][red_idx]
                pre = lst[s][red_idx-1]
                lst[s][red_idx] = pre
                lst[s][red_idx-1] = red
                red_idx -= 1

        while lst[s_b][blue_idx-1] != '#':
               blue = lst[s_b][blue_idx]
               pre = lst[s_b][blue_idx-1]
               lst[s_b][blue_idx] = pre
               lst[s_b][blue_idx-1] = blue
               blue_idx -= 1

    return lst, s, red_idx, s_b, blue_idx, 'left'

def right(lst):
    for i in range(len(lst)):
        if 'R' in lst[i]:
            s = i

    red_idx = lst[s].index('R')
    #blue 위치
    for i in range(len(lst)):
        if 'B' in lst[i]:
            s_b = i

    blue_idx = lst[s_b].index('B')

    if s == s_b:
        if red_idx > blue_idx:

            while lst[s][red_idx+1] != '#':
                red = lst[s][red_idx]
                pre = lst[s][red_idx+1]
                lst[s][red_idx] = pre
                lst[s][red_idx+1] = red
                red_idx += 1

            while lst[s_b][blue_idx+1] != '#':
                blue = lst[s_b][blue_idx]
                pre = lst[s_b][blue_idx+1]
                lst[s_b][blue_idx] = pre
                lst[s_b][blue_idx+1] = blue
                blue_idx += 1
        
        elif red_idx < blue_idx:

            while lst[s_b][blue_idx+1] != '#':
                blue = lst[s_b][blue_idx]
                pre = lst[s_b][blue_idx+1]
                lst[s_b][blue_idx] = pre
                lst[s_b][blue_idx+1] = blue
                blue_idx += 1

            while lst[s][red_idx+1] != '#':
                red = lst[s][red_idx]
                pre = lst[s][red_idx+1]
                lst[s][red_idx] = pre
                lst[s][red_idx+1] = red
                red_idx += 1
    else:
        while lst[s][red_idx+1] != '#':
                red = lst[s][red_idx]
                pre = lst[s][red_idx+1]
                lst[s][red_idx] = pre
                lst[s][red_idx+1] = red
                red_idx += 1

        while lst[s_b][blue_idx+1] != '#':
               blue = lst[s_b][blue_idx]
               pre = lst[s_b][blue_idx+1]
               lst[s_b][blue_idx] = pre
               lst[s_b][blue_idx+1] = blue
               blue_idx += 1

    return lst, s, red_idx, s_b, blue_idx, 'right'

    


def down(lst):
    for i in range(len(lst)):
        if 'R' in lst[i]:
            s = i

    red_idx = lst[s].index('R')

    #blue 위치
    for i in range(len(lst)):
        if 'B' in lst[i]:
            s_b = i

    blue_idx = lst[s_b].index('B')

    if red_idx == blue_idx:
        if s > s_b:

            while lst[s+1][red_idx] != '#':                    
                red = lst[s][red_idx]
                pre = lst[s+1][red_idx] 
                lst[s][red_idx] = pre
                lst[s+1][red_idx] = red
                s += 1

            while lst[s_b+1][blue_idx] != '#':
                blue = lst[s_b][blue_idx]
                pre = lst[s_b+1][blue_idx] 
                lst[s_b][blue_idx] = pre
                lst[s_b+1][blue_idx] = blue
                s_b += 1
        
        elif s < s_b:

            while lst[s_b+1][blue_idx] != '#':
                blue = lst[s_b][blue_idx]
                pre = lst[s_b+1][blue_idx] 
                lst[s_b][blue_idx] = pre
                lst[s_b+1][blue_idx] = blue
                s_b += 1

            while lst[s+1][red_idx] != '#':
                red = lst[s][red_idx]
                pre = lst[s+1][red_idx] 
                lst[s][red_idx] = pre
                lst[s+1][red_idx] = red
                s += 1
    else:
        while lst[s_b+1][blue_idx] != '#':
                blue = lst[s_b][blue_idx]
                pre = lst[s_b+1][blue_idx] 
                lst[s_b][blue_idx] = pre
                lst[s_b+1][blue_idx] = blue
                s_b += 1

        while lst[s+1][red_idx] != '#':
            red = lst[s][red_idx]
            pre = lst[s+1][red_idx] 
            lst[s][red_idx] = pre
            lst[s+1][red_idx] = red
            s += 1

    return lst, s, red_idx, s_b, blue_idx, 'down'

def up(lst):
    for i in range(len(lst)):
        if 'R' in lst[i]:
            s = i

    red_idx = lst[s].index('R')
    #blue 위치
    for i in range(len(lst)):
        if 'B' in lst[i]:
            s_b = i

    blue_idx = lst[s_b].index('B')

    if red_idx == blue_idx:
        if s < s_b:

            while lst[s-1][red_idx] != '#':                    
                red = lst[s][red_idx]
                pre = lst[s-1][red_idx] 
                lst[s][red_idx] = pre
                lst[s-1][red_idx] = red
                s -= 1

            while lst[s_b-1][blue_idx] != '#':
                blue = lst[s_b][blue_idx]
                pre = lst[s_b-1][blue_idx] 
                lst[s_b][blue_idx] = pre
                lst[s_b-1][blue_idx] = blue
                s_b -= 1
        
        elif s > s_b:

            while lst[s_b-1][blue_idx] != '#':
                blue = lst[s_b][blue_idx]
                pre = lst[s_b-1][blue_idx] 
                lst[s_b][blue_idx] = pre
                lst[s_b-1][blue_idx] = blue
                s_b -= 1

            while lst[s-1][red_idx] != '#':
                red = lst[s][red_idx]
                pre = lst[s-1][red_idx] 
                lst[s][red_idx] = pre
                lst[s-1][red_idx] = red
                s -= 1
    else:
        while lst[s_b-1][blue_idx] != '#':
                blue = lst[s_b][blue_idx]
                pre = lst[s_b-1][blue_idx] 
                lst[s_b][blue_idx] = pre
                lst[s_b-1][blue_idx] = blue
                s_b -= 1

        while lst[s-1][red_idx] != '#':
            red = lst[s][red_idx]
            pre = lst[s-1][red_idx] 
            lst[s][red_idx] = pre
            lst[s-1][red_idx] = red
            s -= 1

    return lst, s, red_idx, s_b, blue_idx, 'up'

   

##red 위치
for i in range(len(lst)):
    if 'R' in lst[i]:
        s = i
red_idx = lst[s].index('R')

lst[s][red_idx]

#blue 위치
for i in range(len(lst)):
       if 'B' in lst[i]:
           s_b = i
blue_idx = lst[s_b].index('B')

lst[s_b][blue_idx]

#O위치
for i in range(len(lst)):
    if 'O' in lst[i]:
        e = i
o_idx = lst[e].index('O')

lst[e][o_idx]



proc = []
cnt = 0
while lst[e][o_idx] == 'O':

    if lst[s][red_idx+1] =='O':
        lst, s,red_idx, s_b, blue_idx, p = right(lst)
        proc.append(p)
        cnt += 1
        if lst[s_b][blue_idx+1] == 'R' or lst[s_b][blue_idx-1] == 'R':
            cnt = -1
            
            break  
        
        break
        
    if lst[s][red_idx-1] =='O':
        lst, s,red_idx, s_b, blue_idx, p = left(lst)
        proc.append(p)
        cnt += 1
        if lst[s_b][blue_idx+1] == 'R' or lst[s_b][blue_idx-1] == 'R':
            cnt = -1
            break  
        break

    if lst[s+1][red_idx] == 'O':
        lst, s,red_idx, s_b, blue_idx, p = down(lst)
        proc.append(p)
        cnt += 1
        if lst[s_b+1][blue_idx] == 'R' or lst[s_b-1][blue_idx] == 'R':
            cnt = -1
            break  
        break
    if lst[s-1][red_idx] == 'O':
        lst, s,red_idx, s_b, blue_idx, p = up(lst)
        proc.append(p)
        cnt += 1
        if lst[s_b+1][blue_idx] == 'R' or lst[s_b-1][blue_idx] == 'R':
            cnt = -1
            break  
        break

    if lst[s][red_idx+1] == '.':
        lst, s,red_idx, s_b, blue_idx, p = right(lst)
        proc.append(p)
        
        cnt += 1
     
    elif lst[s][red_idx-1] == '.':
        lst, s, red_idx, s_b, blue_idx, p = left(lst)
        proc.append(p)
        
        cnt += 1
        
    if lst[s+1][red_idx] == '.':
        lst, s,red_idx, s_b, blue_idx, p = down(lst)
        proc.append(p)
        
        cnt += 1
       
    elif lst[s-1][red_idx] == '.':
        lst, s,red_idx, s_b, blue_idx, p = up(lst)
        proc.append(p)
        
        cnt += 1
      
    if cnt >40:
        cnt = -1
        break


di = {'down':0, 'up': 0, 'right':1, 'left':1}

proc_num = []
for i in range(len(proc)):
    proc_num.append(di[proc[i]])


proc_num2 = proc_num.copy()
for i in range(1, len(proc_num)):
    if proc_num[i-1] == proc_num[i]:
        proc_num2[i] = 'a'

while 'a' in proc_num2:
    proc_num2.remove('a')

proc_num2



if proc[-1] == 'left' or 'right':
    if lst[s_b][blue_idx+1] == 'R' or lst[s_b][blue_idx-1] == 'R':
            cnt = -1
    
if proc[-1] == 'down' or 'up':
    if lst[s_b+1][blue_idx] == 'R' or lst[s_b-1][blue_idx] == 'R':
            cnt = -1

if cnt == -1:
    print(-1)
else:
    print(len(proc_num2))


print(proc)




