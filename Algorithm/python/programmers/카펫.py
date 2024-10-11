def solution(brown, yellow):
    brown = (brown-4)//2
    
    answer = [0, 0]
    for a in range(1, (brown//2)+1):
        b = brown - a
        if a * b == yellow:
            answer = [a, b]
            break
        
    
    answer[0] += 2
    answer[1] += 2
    answer.sort(reverse=True)
    return answer