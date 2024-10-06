def rec(answer,p):
    if p == "":
        return answer
    
    u,v = div(p)
    # print(f"u:{u}, v:{v}, answer:{answer}")
    if check(u):
        answer += u
        answer = rec(answer,v)
    else:
        pre = "(" + rec("",v) + ")"
        end = ""
        for i in u[1:len(u)-1]:
            if i == "(":
                end += ")"
            else:
                end += "("
                
        answer += (pre+end)
    
    return answer

def div(w):
    cnt_map = {"(":0,")":0}
    u = ""
    v = ""
    for i in range(len(w)):
        cnt_map[w[i]] += 1
        u += w[i]
        if cnt_map["("] and cnt_map[")"] and cnt_map["("] == cnt_map[")"]:
            break
    v = w[i+1:]
    return u,v

def check(w):
    if w[0] == ")":
        return False
    
    stack = [w[0]]
    
    for i in range(1,len(w)):
            
        if stack and stack[-1] == "(" and w[i] == ")":
            stack.pop()
        else:
            stack.append(w[i])
    
    if stack:
        return False
    
    return True


def solution(p):
    
    answer = rec("",p)
    
    return answer