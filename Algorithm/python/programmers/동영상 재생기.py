def solution(video_len, pos, op_start, op_end, commands):

    def trans(string):
        hour, minute = [int(i) for i in string.split(":")]
        return (hour * 60) + minute
        
    video_len = trans(video_len)
    current = trans(pos)
    op_start = trans(op_start)
    op_end = trans(op_end)
    
    if op_start <= current <= op_end:
        current = op_end
    
    def move_next():
        nonlocal video_len, current, op_start, op_end
        current = min(video_len, current + 10)
        
        if op_start <= current <= op_end:
            current = op_end
    
    def move_prev():
        nonlocal video_len, current, op_start, op_end
        current = max(0, current - 10)
        
        if op_start <= current <= op_end:
            current = op_end
    
    for command in commands:
        
        if command == "next":
            move_next()
        elif command == "prev":
            move_prev()
        
        # print(f"{command} -> {current//60}:{current%60}")
    hour = str(current//60)
    if len(hour) == 1:
        hour = "0" + hour
    
    minutes = str(current%60)
    if len(minutes) == 1:
        minutes = "0" + minutes
    answer = hour + ":" + minutes
    return answer