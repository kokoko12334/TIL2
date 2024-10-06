n = int(input())

def gaps(n):
    i= 0
    if len(str(n))<=2:
        return n
    else:
        i = 99
        for j in range(100, n+1):
            j_lst = list(map(int,str(j)))
            a1 = j_lst[1]-j_lst[0]
            a2 = j_lst[2]-j_lst[1]
            
            if a1 == a2:
                i += 1
        return i
print(gaps(n))



######다른 답안
n = input()
count = 0
for i in range(1,int(n)+1):
    num = list(map(int,str(i)))
    if i<100:
        count += 1
    elif (num[0]-num[1]) == (num[1]-num[2]) :
        count+=1
             
print(count)


