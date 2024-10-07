def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

N = int(input())
buildings = list(map(int, input().split()))

result = 0
for i1, y1 in enumerate(buildings):
    x1 = i1 + 1  # 빌딩의 위치를 1부터 시작한다고 가정

    # 오른쪽 볼 수 있는 빌딩 수
    cur_slope_right = float('-inf')  # 초기화
    visible_right = 0
    for i2 in range(i1 + 1, N):
        x2 = i2 + 1
        y2 = buildings[i2]
        slope_right = slope(x1, y1, x2, y2)

        if cur_slope_right < slope_right:  # 이전 기울기보다 클 경우만
            cur_slope_right = slope_right
            visible_right += 1

    # 왼쪽 볼 수 있는 빌딩 수
    cur_slope_left = float('inf')  # 초기화
    visible_left = 0
    for i3 in range(i1 - 1, -1, -1):
        x2 = i3 + 1
        y2 = buildings[i3]
        slope_left = slope(x1, y1, x2, y2)

        if cur_slope_left > slope_left:  # 이전 기울기보다 작을 경우만
            cur_slope_left = slope_left
            visible_left += 1

    # 현재 빌딩에서 볼 수 있는 빌딩 수 업데이트
    result = max(result, visible_left + visible_right)

print(result)
