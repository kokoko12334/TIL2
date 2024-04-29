def kmp_search(text, pattern):
    # 실패 함수를 구성
    pi = compute_pi(pattern)
    j = 0  # 패턴의 인덱스
    n_text = len(text)
    n_pattern = len(pattern)
    found_indexes = []

    # 전체 텍스트를 순회
    for i in range(n_text):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]

        if text[i] == pattern[j]:
            if j == n_pattern - 1:
                # 패턴이 일치하는 위치를 찾음
                found_indexes.append(i - j)
                j = pi[j]
            else:
                j += 1

    return found_indexes

def compute_pi(pattern):
    n = len(pattern)
    pi = [0] * n # 접두사 테이블 초기화
    j = 0 # 접두사의 길이
    
    # i는 1부터 문자열의 끝까지 반복
    for i in range(1, n):
        # j > 0이고 현재 문자가 접두사의 다음 문자와 일치하지 않는 경우
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1] # j를 감소시키면서 일치하는 위치를 찾음 => 그다음 접두사,접미사 부분을 확인

        # 현재 문자가 접두사의 다음 문자와 일치하는 경우
        if pattern[i] == pattern[j]:
            j += 1 # 접두사 길이를 증가
            pi[i] = j # 해당 위치에 접두사 길이를 저장

    return pi

string = "abdabdabc"
pattern = "abdabc"
pattern_start = kmp_search(string, pattern)

n_pattern = len(pattern)
for start in pattern_start:
    end = start + n_pattern
    print(string[start:end])