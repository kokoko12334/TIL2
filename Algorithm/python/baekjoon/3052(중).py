lst = []
for i in range(10):
    a = int(input())
    result = a%42
    lst.append(result) 

i = 0 
cnt = 0
while len(lst) > 0:          #lst가 빈리스트가 아니면 실행
    print(lst)
    r = lst[i]
    if lst.count(r) == 1:     #요소의 갯수가 1이면 다음 실행
        lst.remove(r)      
        cnt +=1  
    else:
        lst = [item for item in lst if item != r]  #해당요소의 값들을 다 삭제
        cnt += 1 
    
print(cnt)



###세트로 풀기, 중복된 숫자는 세트에서 add가안됨(set는 append대신 add사용함.)
A =set()
for B in range(0,10):
    C = int(input())
    D = C%42
    A.add(D)
print(len(A))


