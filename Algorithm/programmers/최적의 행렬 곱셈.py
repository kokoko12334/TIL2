def solution(matrix_sizes):
    n = len(matrix_sizes)
    
    # DP 테이블 초기화
    dp = [[float('inf')] * n for _ in range(n)]
    
    # 행렬 크기 저장
    sizes = [matrix_sizes[i] for i in range(n)]
    
    # 기본 케이스: 행렬 1개일 때 곱셈 연산은 0
    for i in range(n):
        dp[i][i] = 0
    
    # 길이 2부터 n까지 구간을 늘려가며 DP 테이블 채우기
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # 최소 연산 횟수 계산
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + sizes[i][0] * sizes[k][1] * sizes[j][1]
                if q < dp[i][j]:
                    dp[i][j] = q
    
    # 최종 결과: 모든 행렬을 곱하는데 필요한 최소 곱셈 횟수
    return dp[0][n - 1]

# 예시 사용
matrix_sizes = [[5, 3], [3, 10], [10, 6]]
print(solution(matrix_sizes))  # 270