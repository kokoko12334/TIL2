#https://school.programmers.co.kr/learn/courses/30/lessons/12920
from bisect import bisect_right
def solution(n, cores):
    
    core_n = len(cores)
    if core_n >= n:
        return n
    arr = [(cores[i], i+1) for i in range(core_n)]
    arr.sort(key = lambda x: x[0])
    tasks = n - core_n
    h = 1
    answer = 0
    arr2 = [i[0] for i in arr]
    print(f"arr:{arr}")
    while tasks > 0:
        cnt = bisect_right(arr2, h)
        print(f"남은코어수:{cnt}, h:{h}")
        tasks -= cnt
        print(f"남은 태스크:{tasks}")
        if tasks <= 0:
            answer_idx = cnt + tasks - 1
            answer_arr = sorted(arr[:cnt], key=lambda x: x[1])
            print(f"마지막에서 가장 앞선 코어:{answer_arr}")
            print(f"마지막코어:{answer_idx}")
            answer = answer_arr[answer_idx][1]
            break
        
        h += 1
        
    return answer