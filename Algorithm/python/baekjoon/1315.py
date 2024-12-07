def max_quests(N, quests):
    # 최대 스탯 크기
    MAX_STAT = 1000
    
    # DP 배열 초기화
    DP = [[-1] * (MAX_STAT + 1) for _ in range(MAX_STAT + 1)]
    DP[1][1] = 0  # 초기 상태
    
    # 가능한 상태를 BFS 스타일로 확장
    for str_now in range(1, MAX_STAT + 1):
        for int_now in range(1, MAX_STAT + 1):
            if DP[str_now][int_now] == -1:
                continue
            
            # 현재 상태에서 깰 수 있는 퀘스트를 확인
            current_points = 0
            for str_req, int_req, points in quests:
                if str_now >= str_req or int_now >= int_req:
                    current_points += points
            
            # 현재 상태에서 얻은 포인트를 배분
            for add_str in range(current_points + 1):
                add_int = current_points - add_str
                new_str = min(str_now + add_str, MAX_STAT)
                new_int = min(int_now + add_int, MAX_STAT)
                DP[new_str][new_int] = max(DP[new_str][new_int], DP[str_now][int_now] + 1)
    
    # 모든 상태에서 최대값 계산
    return max(max(row) for row in DP)

# 입력 예제 처리
N = int(input())
quests = []
for _ in range(N):
    quests.append([int(i) for i in input().split()])

print(max_quests(N, quests))  # 4
