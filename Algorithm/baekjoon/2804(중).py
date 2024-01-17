#a가로 b세로

a,b = input().split()
      
for i in range(len(a)):
    for j in range(len(b)):
        
        if a[i]==b[j]:
            a_place = j   #하나씩 훑어가면서 같은 a문자 인덱스는 b의 자리수가 되고 a는 반대임.
            b_place = i 
            break            #j for문만 끝남
    if a[i]==b[j]:   #따라서 i for문을 끝내기 위해서 여기서도 break를 걸어주어야함.
        break

for k in range(len(b)):   #세로 갯수
    if k==a_place:
        print(a)
    else:
        print('.'*(b_place)+b[k]+'.'*(len(a)-(b_place+1)), sep = '\n')   #가로갯수

