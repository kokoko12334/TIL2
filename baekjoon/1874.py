import sys

# num = int(sys.stdin.readline())

# lst = [int(sys.stdin.readline()) for _ in range(num)]

num = int(input())

lst = [int(input()) for _ in range(num)]
line = list(range(1,num+1))[::-1] 

stack = []
result = []

success = True

while True:
        stack.append(line.pop())
        result.append('+')
        if stack[-1] == lst[0]:
            top = stack.pop()
            result.append('-')
            break

for i in range(1, len(lst)):
    if lst[i] == top-1:
        top = stack.pop()
        result.append('-')
    elif lst[i] > top:
        while True:
            stack.append(line.pop())
            result.append('+')
            if stack[-1] == lst[i]:
                top = stack.pop()
                result.append('-')
                break
    else:
        if stack[::-1] == lst[i:]:
            for _ in range(len(stack)):
                result.append('-')
            
            break
        else:
            success = False
            print('NO')
            break       

if success:
    for i in result:
        print(i)










