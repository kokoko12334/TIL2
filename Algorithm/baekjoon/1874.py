import sys
from collections import deque

n = int(input())
answers = []
lst = deque(range(1,n+1))
stack = deque()
lst2 = []
for _ in range(1,n+1):
    answers.append(int(input()))

s = lst.popleft()
stack.append(s)
lst2.append('+')
pr = True
for i in range(len(answers)):
    
    while answers[i] != stack[-1]and len(lst) != 0:
        s = lst.popleft()
        
        stack.append(s)
        lst2.append('+')
    if answers[i] == stack[-1]:
        stack.pop()
        lst2.append('-')
        if not stack and len(lst) != 0:  #스택이 비어있고 lst에 요소가 있다면
            s = lst.popleft()
            stack.append(s)
            lst2.append('+') 
     
   
    elif len(lst) == 0 and stack:
        pr = False
        print('NO')
        break
       

if pr:
    for i in lst2:
        print(i)

###
n = int(input())
stack = []
cnt = 1
ans = []
flag = 1
for _ in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        ans.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        flag = 0

if flag == 0:
    print('NO')
else:
    for a in ans:
        print(a)

