
#피보나치 수열
#공간을 만들고 인덱스로 이미 계산한 정답을 가져옴. 
def fibo(x):
    lst = [0]*(x+1)
    lst[0] = 0
    lst[1] = 1
    for i in range(2, x+1):
        lst[i] = lst[i-2]+lst[i-1]
    return lst[x]


fibo(200)
