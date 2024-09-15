def solution(name):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nn = len(alphabet)
    n = len(name)
    answer = 0
    arr = []
    for i in range(n):
        char = name[i]
        if char != "A":
            arr.append(i)
        idx = alphabet.index(char)
        idx = min(idx, nn-idx)
        answer += idx
        
    print(arr)
    
    
        
    
    return answer