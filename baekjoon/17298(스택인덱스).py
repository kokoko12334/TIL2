import sys


n = int(sys.stdin.readline())

arr = [int(i) for i in sys.stdin.readline().split()]



answer = [-1]*n
stack = []
stack_dic = {}

stack.append(arr[0])
stack_idx = 0
stack_dic[stack_idx] = 0
for i in range(1,len(arr)):
    if stack[-1] >= arr[i]:
        #########################추가
        stack.append(arr[i])
        stack_idx += 1
        stack_dic[stack_idx] = i
        ##############################
    else:
        
        while stack and stack[-1] < arr[i]:
            answer[stack_dic[stack_idx]] = arr[i]
            ######################삭제
            stack.pop()
            stack_idx -= 1
            #########################
        #########################
        stack.append(arr[i])
        stack_idx += 1
        stack_dic[stack_idx] = i
        #############################
        
print(*answer)







