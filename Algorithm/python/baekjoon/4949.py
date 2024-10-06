import sys

a = sys.stdin.readline().split('.')


# a = input().split('.')

a = [i.replace(' ', '') for i in a]


for i in a:
    lst = []
    for j in i:
        if len(j) == 0:
            print('yes')
        else:    
            if j =='[' or j =='(':
                lst.append(j)
            elif j == ']':
                if len(lst) == 0 or lst[-1] != '[':
                    lst.append(']')
                elif lst[-1] == '[':
                    del lst[-1]    
            elif j == ')':
                if len(lst) == 0 or lst[-1] != '(':
                    lst.append(')')
                elif lst[-1] == '(':
                    del lst[-1]  
    if len(lst) == 0:
        print('yes')
    else:
        print('no')




while True :
    a = input()
    stack = []

    if a == "." :
        break

    for i in a :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
            else : 
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')