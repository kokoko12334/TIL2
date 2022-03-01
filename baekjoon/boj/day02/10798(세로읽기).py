

words = [list(input()) for _ in range(5)]

basic = ''

max_length = max([len(words[i]) for i in range(5)]) 
for i in range(max_length):
    for j in range(5):
        try: 
            basic += words[j][i]
        except:
            continue

print(basic)


#########정답
words = [input() for _ in range(5)]
max_len = max(len(word) for word in words) # 가장 긴 문자열을 기준으로 설정

for i in range(max_len):
    for word in words:
        if i < len(word): # 길이가 짧은 문자열에 대해 에러 방지
            print(word[i], end="")

