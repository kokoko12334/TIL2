MOD = 1000000

def zigzag_permutations(N):
    # Up과 Down 배열 초기화
    Up = [[0] * (N + 1) for _ in range(N + 1)]
    Down = [[0] * (N + 1) for _ in range(N + 1)]
    
    # 길이 1인 순열의 초기값 설정 (첫 번째 수가 a인 경우)
    for i in range(1, N + 1):
        Up[1][i] = 1
        Down[1][i] = 1

    # DP 테이블 채우기
    for n in range(3, N + 1, 2):  # 길이 n에 대해 계산
        for a in range(1, N + 1):  # 첫 번째 수 a에 대해
            for b in range(a + 1, N + 1):  # b는 a보다 큰 수
                for i in range(1, b - 1):  # b 다음에 올 수 있는 수
                    Up[n][a] = (Up[n][a] + Up[n - 2][i]) % MOD
    
    # 최종 결과 계산
    result = 0
    for i in range(1, N):  # Up의 경우
        result = (result + Up[N][i]) % MOD
    
    for i in range(2, N + 1):  # Down의 경우
        result = (result + Down[N][i]) % MOD
    
    return result

# 입력
N = int(input())

# 출력
print(zigzag_permutations(N))
