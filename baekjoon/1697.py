import sys

n, k = [int(i) for i in sys.stdin.readline().split()]

lst = [n]
sec = 0 
if n == k:
    print(sec)
elif n<k:    
    enter = True
    check = {}
    
    while enter:
        lst2 = []
        sec += 1
        for i in lst:
            back = i-1
            if back not in check and back<= 100000:
                lst2.append(back)
                check[back] = True
            if back == k:
                enter = False
                break   
            walk = i+1
            if walk not in check and walk <= 100000:
                lst2.append(walk)
                check[walk] = True
            if walk == k:
                enter = False
                break   
            tele = i*2
            if tele not in check and tele<= 100000:
                lst2.append(tele)
                check[tele] = True
            if tele == k:
                enter = False
                break
        
        lst = lst2
        
else:
    sec = n-k               
print(sec)
