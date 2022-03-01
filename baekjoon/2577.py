lst = []
for i in range(3):
    a = int(input())
    lst.append(a)         #3개의 변수를 한줄 씩 받기

r = 1
for i in lst:
    r *= i            #세개의 곱의 결과 값


r_str = str(r)        #count를 쓰기 위해서 str로 변경

for i in range(10):       #count로 갯수 새기
    cnt = r_str.count(str(i))
    print(cnt)


#count는 int의 메소드가 아니고 
#만약에 객체가 str이면 매개변수도 str이 되어야 한다.

