
a, b, c = [int(i) for i in input().split()]

def div(a, b, c):

    if b == 1:
        return a % c
    
    tmp = div(a, b//2, c)
    
    if b % 2 == 1:
        return ((tmp * tmp * a) % c)
    else:
        return (tmp * tmp) % c

print(div(a, b, c))
