# # 없으면 -1
def mul(expression):

    idx = expression.find("*")
    while idx != -1:
        r = idx - 1
        l = idx + 1
        flag1 = False
        flag2 = False
        while r > 0 and expression[r] not in {"*","-","+"} :
            r -= 1
            
                
        while l < len(expression) and expression[l] not in {"*","-","+"}:
            l += 1
        if expression[r:l+1][0] in {"*", "-","+"}:    
            r += 1
        if expression[r:l+1][-1] in {"*", "-","+"}:    
            l -= 1
        
        
        cal = expression[r:l+1]
        a, b = [int(i) for i in cal.split("*")]
        c = str(a*b)
        expression = expression[:r] + c + expression[l+1:]
        idx = expression.find("*")
    
    return expression


def sub(expression):
    
    idx = expression.find("-")
    while idx > 0:
        r = idx - 1
        l = idx + 1
        flag1 = False
        flag2 = False
        while r > 0 and expression[r] not in {"*","-","+"} :
            r -= 1
            
                
        while l < len(expression) and expression[l] not in {"*","-","+"}:
            l += 1
        if expression[r] in {"*", "-","+"}:    
            r += 1
        if expression[l] in {"*", "-","+"}:    
            l -= 1
        
        
        cal = expression[r:l+1]
        a, b = [int(i) for i in cal.split("-")]
        c = str(a-b)
        expression = expression[:r] + c + expression[l+1:]
        idx = expression.find("-")
    
    return expression

sub("50*6-3*2")
sub("100-200*300-500+20")
0.06*0.02*100