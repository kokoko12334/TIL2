def solution(routes):
    n = len(routes)
    routes.sort(key=lambda x: (x[0], -x[1]))
    s = 0
    idx = 1
    answer = 1
    num = routes[s][1]

    while idx < n:
        if num >= routes[idx][0]:
            if num > routes[idx][1]:
                num = routes[idx][1]
        else:
            answer += 1
            num = routes[idx][1]
        idx += 1
    return answer