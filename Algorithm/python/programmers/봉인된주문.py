
def solution(n, bans):
    answer = ''
    alp_map = {i: (ord(i) - 96) for i in "abcdefghijklmnopqrstuvwxyz"}
    alp_map_rev = {v: k for k, v in alp_map.items()}
    bans.sort(key = lambda x: (len(x), x))

    def trans(string):
        nn = len(string)
        num = 0
        for i in range(nn):
            num += (26 ** (nn - i - 1)) * alp_map[string[i]]
        return num

    for al in bans:
        num = trans(al)
        # print(f"{al} -> {num}")
        if num <= n:
            n += 1
    arr = []
    while n > 0:
        res = n % 26
        if res == 0:
            arr.append(alp_map_rev[26])
            n = (n // 26) - 1
        else:
            arr.append(alp_map_rev[res])
            n = n // 26
            
    # print((10**15)//26)
    # print(arr)
    return "".join(arr[::-1])