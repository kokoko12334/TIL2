class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        pi = [0] * n  # 접두사 테이블 초기화
        j = 0  # 접두사의 길이

        # i는 1부터 문자열의 끝까지 반복
        for i in range(1, n):
            # j > 0이고 현재 문자가 접두사의 다음 문자와 일치하지 않는 경우
            while j > 0 and s[i] != s[j]:
                j = pi[j - 1]  # j를 감소시키면서 일치하는 위치를 찾음 => 그다음 접두사,접미사 부분을 확인

            # 현재 문자가 접두사의 다음 문자와 일치하는 경우
            if s[i] == s[j]:
                j += 1  # 접두사 길이를 증가
                pi[i] = j  # 해당 위치에 접두사 길이를 저장
            else:
                pi[i] = 0  # 일치하지 않으면 0을 저장

        nn = pi[-1]
        answer = s[(n-1)-(nn-1):n]
        print(pi)
        return answer


a = Solution()

print(a.longestPrefix("ABCDABD"))