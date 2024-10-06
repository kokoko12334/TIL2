def trans(string):
    time = [int(i) for i in string.split(":")]
    
    return time[0] * 60 + time[1]

def reverse(time):
    h = time//60
    m = time%60
    if h < 10:
        h = "0" + str(h)
    else:
        h = str(h)
    if m < 10:
        m = "0" + str(m)
    else:
        m = str(m)
    return h + ":" + m

def solution(n, t, m, timetable):
    
    interval = [0] * n
    timetable_trans = sorted([trans(i) for i in timetable])
    time = trans("9:00")

    for i in range(n):
        interval[i] = time
        time += t
    
    avail = {i:[] for i in interval}
    idx = 0
    bus = interval[idx]
    for i in timetable_trans:
        flag = True
        # print(f"사람:{i}")
        while i > bus or len(avail[bus]) == m:
            # print(f"탑승불가능:{bus},이유는 시간이 안됨:{i> bus}, 이유는 인원참:{len(avail[bus]) == m}")
            idx += 1
            if idx >= len(interval):
                flag = False
                break
            bus = interval[idx]
            
        # print(f"탑승 버스:{bus},flag:{flag} 현재인원:{avail[bus]}")
        if flag:
            avail[bus].append(i)
    
    last_bus = avail[interval[-1]]
    
    if len(last_bus) < m:
        return reverse(interval[-1])
    
    return reverse(last_bus[-1] - 1)