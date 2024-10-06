def solution(book_time):
    events = []
    
    for start, end in book_time:
        # 시작 시각을 분으로 변환
        start_h, start_m = map(int, start.split(':'))
        start_minutes = start_h * 60 + start_m
        
        # 종료 시각을 분으로 변환
        end_h, end_m = map(int, end.split(':'))
        end_minutes = end_h * 60 + end_m
        
        # 객실 사용 시작
        events.append((start_minutes, 1))  # 예약 시작
        # 퇴실 후 청소 시간 고려 (10분 뒤)
        events.append((end_minutes + 10, -1))  # 예약 종료 + 청소 시간
        
    # 시간순으로 정렬
    events.sort()
    
    max_rooms = 0
    current_rooms = 0
    
    for time, change in events:
        current_rooms += change
        max_rooms = max(max_rooms, current_rooms)
        
    return max_rooms