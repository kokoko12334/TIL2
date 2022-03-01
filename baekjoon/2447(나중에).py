a = int(input())

def star(x):
    print('*'*x)
    if x ==0:
        return 
    star(x-1)


star(3)

