
#https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3

def solution(s):
    puzzle = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    for k, v in puzzle.items():
        v = str(v)
        s=s.replace(k,v)
        
    return int(s)

solution("one4seveneight")










