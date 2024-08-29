def solution(begin, end):
    answer = []
    for num in range(begin, end+1):
        if num == 1:
            answer.append(0)
            continue
        num2 = int((num**(1/2)))
        result = 1
        
        for i in range(2, num2+1):
            
            if num%i == 0:
                # print(i)
                if num//i <= 10000000:
                    result = num//i
                    break
                else:
                    result = max(result, i)
                    continue
        answer.append(result)
    
    return answer