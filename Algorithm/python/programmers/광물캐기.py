
def solution(picks, minerals):
    values = {
        "diamond": 25,
        "iron": 5,
        "stone": 1
    }
    cost = [
        {"diamond": 1, "iron": 1, "stone": 1},
        {"diamond": 5, "iron": 1, "stone": 1},
        {"diamond": 25, "iron": 5, "stone": 1},
    ]
    n = len(minerals)
    arr = []
    arr2 = []
    cnt = 0
    for i in range(0,n,5):
        summ = sum([values[minerals[j]] for j in range(i, i + 5) if j < n])
        arr.append((summ, cnt))
        arr2.append([minerals[j] for j in range(i, i + 5) if j < n])
        cnt += 1
    
    if len(arr) <= sum(picks):
        arr.sort()
    else:
        dis = len(arr) - sum(picks)
        arr = arr[:len(arr) - dis]
        arr.sort()
    pick = 0
    answer = 0
    while pick <= 2 and arr:
        if picks[pick] != 0:
            picks[pick] -= 1
        else:
            pick += 1
            continue
        value, m_idx = arr.pop()
        mineral = arr2[m_idx]
        summ = 0
        for m in mineral:
            summ +=cost[pick][m]
        answer += summ
    

    return answer