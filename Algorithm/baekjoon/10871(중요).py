
n,x = map(int, input().split())

A = list(map(int, input().split()))  #입력한 갯수만큼 받음.

for i in range(len(A)):
    if A[i] < x:
        print(A[i], end=" ")










