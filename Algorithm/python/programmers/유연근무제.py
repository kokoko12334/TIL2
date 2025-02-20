def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        hour = schedules[i] // 100
        minn = schedules[i] % 100
        
        if minn + 10 > 59:
            hour += 1
            minn = (minn + 10) % 60
            work_time = (hour * 100) + minn
        else:
            work_time = schedules[i] + 10
            
        flag = True
        for j in range(7):
            if (startday + j) % 7 in {6, 0}:
                continue
            
            if timelogs[i][j] > work_time:
                flag = False
                break
        if flag:
            answer += 1

    return answer