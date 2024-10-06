import math

n = int(input())
a = [int(i) for i in input().split()]
b,c = [int(i) for i in input().split()]

math.ceil(1.1)
answer = n
for i in a:
    num = i-b
    if num > 0:
        answer += math.ceil(num/c) 
print(answer)
