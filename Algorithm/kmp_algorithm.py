def kmp_search(text, pattern):
    # 실패 함수를 구성
    pi = compute_pi(pattern)
    j = 0  # 패턴의 인덱스
    found_indexes = []

    # 전체 텍스트를 순회
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]

        if text[i] == pattern[j]:
            if j == len(pattern) - 1:
                # 패턴이 일치하는 위치를 찾음
                found_indexes.append(i - j)
                j = pi[j]
            else:
                j += 1

    return found_indexes

def compute_pi(pattern):
    pi = [0] * len(pattern)
    j = 0

    # 패턴의 각 문자에 대해 실패 함수를 계산
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

    return pi


