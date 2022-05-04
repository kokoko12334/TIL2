
#CountVectorizer
# 해당 단어의 중복을 제외시키고 사전을 만든다음 해당 문장을 벡터수치로 변환
from sklearn.feature_extraction.text import CountVectorizer

text= ['나는 배가 고프다', '내일 점심 머먹지', '내일 공부 해야겠다','점심 먹고 공부 해야지']

cv = CountVectorizer()   #객체화
cv.fit(text) #사전

word2idx = cv.vocabulary_  #사전 조회
word2idx

idx2word={v:k for k,v in word2idx.items() }  #사전조회(인덱스가 키값)
idx2word

##문장 벡터화
sentence = [text[0]]
cv.transform(sentence).toarray()
print(cv.transform(text).toarray())





#TfidfVectorizer
#코랩 자연어처리1일차에서 설명 확인
from sklearn.feature_extraction.text import TfidfVectorizer


tfidf_v = TfidfVectorizer()
tfidf_v.fit(text)  #사전 생성
print(tfidf_v.vocabulary_)

sentence = [text[3]]
print(tfidf_v.transform(sentence).toarray())
#역수 취하고 로그를 계산한거임







#HashingVectorizer

from sklearn.feature_extraction.text import HashingVectorizer


hash_v = HashingVectorizer(n_features = 10)  #10 = len(word2idx)
hash_v.fit(text)
#사전이 아니라 해쉬함수 기반이라서 .vocabulary_하면 에러가 난다. n_feature는 사전의 갯수를 말한다.

print(hash_v.transform(sentence).toarray())























