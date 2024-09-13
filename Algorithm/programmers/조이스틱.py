
def solution(name):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = len(alphabet)
    answer = 0
    for char in name:
        idx = alphabet.index(char)
        idx = min(idx, n-idx)
        answer += idx
        print(f"char:{char}, idx:{idx}")
        
    print(answer)
    return answer