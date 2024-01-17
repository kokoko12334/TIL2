
lst = [1,2,3]

lst2 = lst
lst is lst2  #같은 포인터를 가리키므로 객체(가리키는것)가 같음
#이는 수정시에 lst도 같이 수정됨



###map대신 리스트컴프리헨션을 이용 더 빠르다고 함.(한 줄에만 받는거)
n = [int(i) for i in input().split()] 
n = [int(i) for i in input()]

###2차원 리스트 받기(컴프리헨션)

#일반적인 형태
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
print(board)

#(컴프리헨션)
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)] #리스안의 리스트
print(board)

lst = [int(input()) for _ in range(n)]  #리스트안에 요소들 #split 없이

#더 축약

board = [list(map(int, input().split())) for _ in range(int(input()))]
print(board)



###############조건의 정렬
a = [('a',5),('b',3),('c',4)]

sorted(a, key=lambda x:x[1])       #x에서 [1]을 기준으로 정렬하라.




#zip
#같은 인덱스의 값끼리 튜플로 묶어둠.
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]


list(zip(a,b,c))

















