def solution(gems):
    answer = []
    gem_sett = set()
    for g in gems:
        gem_sett.add(g)
    # print(gem_sett)
    answer_cnt = len(gem_sett)
    n = len(gems)
    gems_idx = {}
    cnt = 0
    answers = []
    for i in range(n):
        gem = gems[i]
        if gem in gems_idx.keys():
            half = n//2
            original = abs(gems_idx[gem]-half)
            new = abs(i-half)
            if new < original:
                gems_idx[gem] = i
        else:
            gems_idx[gem] = i
            cnt += 1
        if cnt == answer_cnt:
            arr = gems_idx.values()
            print(gems_idx)
            maxx = max(arr)
            minn = min(arr)
            dif = maxx-minn
            answers.append([dif,minn+1,maxx+1])
    answers.sort(key=lambda x: x[0])
    answer = answers[0]
    return answer