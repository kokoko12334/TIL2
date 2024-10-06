def solution(s):
    stack = []
    for i in range(len(s)):
        alphabet = s[i]
        if not stack:
            stack.append(alphabet)
            continue
        
        if stack[-1] == alphabet:
            stack.pop()
        else:
            stack.append(alphabet)
        
    if stack:
        return 0
    else:
        return 1