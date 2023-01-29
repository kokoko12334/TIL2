import sys

brack = sys.stdin.readline()


brack = brack.replace("()", "ll")



stack = []
idx_dic = {}

lst = []
stack_idx = 0
for i in range(len(brack)):
    if brack[i] == 'l':
        pass
    else:
        if not stack:
            idx_dic[stack_idx] = i
            stack.append(brack[i])
            stack_idx += 1
        else:
            
            if stack[-1] == "(" and brack[i] == ")":
                lst.append([idx_dic[len(stack)-1],i])
                stack.pop()
                stack_idx -= 1
                
            else:
                idx_dic[stack_idx] = i
                stack.append(brack[i])
                stack_idx += 1


answer = 0
for i in lst:

    new_str = brack[i[0]:i[1]+1]
    
    answer += (new_str.count('l')/2)+1


print(int(answer))



