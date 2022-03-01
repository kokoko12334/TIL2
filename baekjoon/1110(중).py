a = int(input())

def trans(a):
    
    a_str = str(a)  #문자화

    if len(a_str) == 1:
        a_str = a_str.zfill(2)  #a가 1의자리수면 왼쪽에 0추가

    a_dot = '.'.join(a_str)    #문자열 사이에 '.' 추가

    a_sep = a_dot.split('.')   # '.'을 기준으로 분리

    b = int(a_sep[0])+int(a_sep[1])  #문자열인 a의 인덱스1과 인덱스2를 합침.

    b_str = str(b) #b는 정수이므로 문자열화

    if len(b_str) == 1:
        b_str = b_str.zfill(2)   #b가 1의 자리수면 왼쪽에 0추가

    r = int(a_sep[1]+b_str[1]) #a의 두번째 자리와 b의 두번째자리의 합

    return r

i = 0
b = a    #a는 수시로 바뀌게 되어서 b에 저장(초기값을 저장)
while True:
    a1 = trans(a)
    i += 1
    print(f'입력값:{b}, 변화는 값:{a1}')
    if b == a1:
        print(i)
        break
    a = a1        #a1을 다시 a에 넣어서 trans(a)를 계속 시행함.
    
 

##클래스로 만들어 본것
class Trans:
    def __init__(self, a):
        self.a = a
    
    def trans(self):
        self.a_str = str(self.a)

        if len(self.a_str) == 1:
            self.a_str = self.a_str.zfill(2) 

        self.a_dot = '.'.join(self.a_str) 

        self.a_sep = self.a_dot.split('.') 

        b = int(self.a_sep[0])+int(self.a_sep[1]) 

        b_str = str(b) 

        if len(b_str) == 1:
            b_str = b_str.zfill(2)  

        r = int(self.a_sep[1]+b_str[1])

        return r

a =26

a1 = Trans(a).trans()





#숏코딩

n=int(input())
m,i=n,0
while m != n or i==0:   #처음에는 m=n이 되어버리니까 i==0으로 해서 while문에 들어감.
  i+= 1
  n=(n%10)*10+(n//10+n%10)%10
print(i)

