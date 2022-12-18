n = int(input())

def log3(n):
    cnt = 0
    while n > 1:
        cnt += 1
        n = n/3
    return cnt

nn = log3(n)    
#중앙을 비워두고 둘러쌈
#재귀함수에서 반복할 만한거 찾고 초기값 설정함.

def appendd(lst):
    if lst == '*':
        empty = ' '*len(lst)
        ent = '\n'

        space = [lst,lst,lst,ent,lst,empty,lst,ent,lst,lst,lst]

        base = ''.join([i for i in space])
        
        return base
    else:
        space = [lst, lst, lst, ent, lst, empty, lst, ent, lst, lst, lst]

    # result = [space[i:i+3] for i in range(0, 9, 3)]
    # if lst == '*':
    #     space = ''.join([i[0] for i in space])
    #     result = [space[i:i+3] for i in range(0, 9, 3)]
   
    return base
    
def star(n):
    if n == 1:
        return appendd('*')
    
    return appendd(star(n-1))            

n = 1
print(star(n))
star(n)
