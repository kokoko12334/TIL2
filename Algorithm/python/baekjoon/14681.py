#내 답
matrix= []
for i in range(2):
    a=int(input())
    matrix.append(a)

if matrix[0]>0 and matrix[1]>0:
    print(1)
elif matrix[0]>0 and matrix[1]<0:
    print(4)
elif matrix[0]<0 and matrix[1]>0:
    print(2)
else:
    print(3)






