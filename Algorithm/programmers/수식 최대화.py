from itertools import permutations
import re

def cal(arr,exp):
    stack = [arr[0]]
    n = len(arr)
    
    for i in range(1,n):
        
        if stack and stack[-1] == exp:
            
            stack.pop()
            num1 = int(stack.pop())
            num2 = int(arr[i])
            if exp == "+":
                result = num1 + num2
            elif exp == "-":
                result = num1 - num2
            elif exp == "*":
                result = num1 * num2
            stack.append(result)
            
        else:
            
            stack.append(arr[i])
    
    return stack

def solution(expression):
    pattern = r'(\d+|[-+*/])'

    arr = re.findall(pattern, expression)
    exp = set()
    for i in arr:
        if i in {"*","+","-"}:
            exp.add(i)
    cases = list(permutations(exp,len(exp)))
    
    
    answer = 0
    for c in cases:
        arr2 = arr[:]
        for exp in c:
            arr2 = cal(arr2,exp)
            
        val = abs(arr2[0])
        
        if answer < val:
            answer = val
    
    return answer



