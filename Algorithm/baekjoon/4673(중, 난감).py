# 1~n까지의 자연수 범위중에서 셀프넘버만 리턴하는 함수 만들기
def gen(n):
    i = 1
    set_list = set() #빈 집합
    set_all = set(range(1,n+1))  #1~n까지의 자연수 집합
    while i<=n:
        
        r = i      #1,2,3... 각각의 생성자를 구하기 위해서
        while r <= n:
            r_str = str(r)
            r_sum = sum(map(int, list(r_str))) #자리수 합 구하는 과정
            r += r_sum  #원래 숫자+(자리수합)
            if r <=n:   #n까지 범위를 정헀으므로 다음과 같은 조건을 둠.
                set_list.add(r)  #빈 집합에 추가
        i +=1     #다시 1의 n까지의 생성과정 끝나면 i+=1해서 그다음 2를 진행
    result = set.difference(set_all, set_list) #모든 집합과 생성집합을 빼면 셀프넘버만 남음.
    return result 

#답안형식에 맞게 출력
ko = gen(10000)  #10000까지의 셀프넘버 할당
a1 = list(ko)   #집합을 인덱싱이 안되므로 리스트화
a1.sort()  #리스트화하면 순서가 엉망이되므로 오름차순으로 정렬함
for i in range(len(a1)):       #하나씩 출력
    print(a1[i])

