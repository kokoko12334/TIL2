from itertools import combinations

# 주사위를 선택하는 경우의 수

# 주사위 합의 모든 경우의수

#승패 기록하기

# 가장 높은 승, 패 기록한거 승은 그대로 패배는 all_set - 패배한 경우의수

def get_sum(a_case,b_case,dice):
    
    a_dice = [dice[i] for i in a_case]
    n = len(a_dice) - 1
    a = set()
    a_cnt = {}

    stack = [(i,0) for i in a_dice[0]]
    

    while stack:

        val,level = stack.pop()
        
        if level == n:

            a.add(val)

            if val not in a_cnt:

                a_cnt[val] = 1

            else: 

                a_cnt[val] += 1
        else:
            
            for i in a_dice[level+1]:
                stack.append((val+i,level+1))

    b_dice = [dice[i] for i in b_case]
    n = len(b_dice) - 1
    b = set()
    b_cnt = {}

    stack = [(i,0) for i in b_dice[0]]
    

    while stack:

        val,level = stack.pop()
        
        if level == n:

            b.add(val)

            if val not in b_cnt:

                b_cnt[val] = 1

            else: 

                b_cnt[val] += 1
        else:
            
            for i in b_dice[level+1]:
                stack.append((val+i,level+1))
    
    return a,a_cnt,b,b_cnt

def check(a,a_cnt,b,b_cnt,all_cases):
    a = sorted(a,reverse=True)
    b = sorted(b, reverse=True)
    
    ptr_a = 0
    ptr_b = 0

    n_a = len(a)
    n_b = len(b)

    sum_a = 0
    for v in a_cnt.values():
        sum_a += v
    sum_b = 0
    for v in b_cnt.values():
        sum_b += v
    
    a_win = 0
    b_win = 0
    while ptr_a < n_a and ptr_b < n_b:
        a_v = a[ptr_a]
        b_v = b[ptr_b]

        if a_v > b_v:
            a_win += a_cnt[a_v]*sum_b
            ptr_a += 1
            sum_a -= a_cnt[a_v]

        elif a_v < b_v:
            b_win += b_cnt[b_v]*sum_a
            ptr_b += 1
            sum_b -= b_cnt[b_v]
        else:
            if len(a[ptr_a:]) > len(b[ptr_b:]):
                a_win += a_cnt[a_v]*(sum_b - b_cnt[b_v])
                ptr_a += 1
                sum_a -= a_cnt[a_v]
            else:
                b_win += b_cnt[b_v]*(sum_a - a_cnt[a_v])
                ptr_b += 1
                sum_b -= b_cnt[b_v]
    
    if a_win > b_win:
        return a_win, "a"
    else:
        return b_win, "b"
    

def solution(dice):
    
    # 주사위를 선택하는 경우의 수
    n = len(dice)
    nn = n//2
    all_cases = set(range(n))
    dice_cases = list(map(set,combinations(range(n),nn)))
    nnn = len(dice_cases)//2
    dice_cases = dice_cases[:nnn]
    
    max_win = 0
    answer = []
    for a_case in dice_cases:
        b_case = all_cases - a_case
        a,a_cnt,b,b_cnt = get_sum(a_case,b_case,dice)

        result,winner = check(a,a_cnt,b,b_cnt,all_cases)
        
        if max_win < result:
            max_win = result
            if winner == "a":
                answer = sorted([i+1 for i in a_case])
                
            elif winner == "b":
                answer = sorted([i+1 for i in b_case])
    
    return answer




a = solution([[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]])
print(a)