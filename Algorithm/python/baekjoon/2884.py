
# 시간은 60진수이므로 1.60진수->2.10진수 변환->3.계산->4.60진수 변환
#1. 60진수
h=10
m=10
#2. 10진수 변환
a=h*60+m ;a
#3. 계산
a1=a-45 ; a1
#4. 60진수 변환
h, m = divmod(a1,60)
print(h, m)



#내답 map에서 변수가 두개 이므로 불연산(<= 등등) 가능

h, m = map(int, input().split(' '))  

if h == 0 and m < 45:
    h = 24

time = h*60+m

time_af = time-45

h, m = divmod(time_af, 60)
print(h,m)


#위식에서 if조건문은 0 35 에서 -45하면 h= -1이 나으므로 h=24로 변경

























