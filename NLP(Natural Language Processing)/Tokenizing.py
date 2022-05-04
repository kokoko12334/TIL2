#영어토크나이징

##NLTK
import os
import nltk
os.system('pip install nltk')
nltk.download()

###단어 단위 토크나이징
from nltk.tokenize import word_tokenize

sentence = """
Natural language processing (NLP) is a subfield of computer science, information engineering, 
and artificial intelligence concerned with the interactions between computers and human (natural) languages, 
in particular how to program computers to process and analyze large amounts of natural language data.
"""
print(word_tokenize(sentence))

###문장 단위 토크나이징

from nltk.tokenize import sent_tokenize

paragraph = """
Natural language processing (NLP) is a subfield of computer science, information engineering, 
and artificial intelligence concerned with the interactions between computers and human (natural) languages, 
in particular how to program computers to process and analyze large amounts of natural language data. 
Challenges in natural language processing frequently involve speech recognition, natural language understanding, 
and natural language generation.
"""

print(sent_tokenize(paragraph))

##Spcay

import os
os.system('pip install spacy')
os.system('python -m spacy download en')

import spacy

nlp = spacy.load("en_core_web_sm")#언어 데이터인 en을 불러옴

doc = nlp(sentence) #생성한 객체 값넣기

###단어 단위 토크나이징
word_tokenized_sentence = [token.text for token in doc]
print(word_tokenized_sentence)

###문장 단위 토크나이징
sentence_tokenized_list = [sent.text for sent in doc.sents]
print(sentence_tokenized_list)




# 한글 토크나이징

## KoNLPy
import os #터미널에서 진행하는게 좋음
import sys #파이썬 버전 확인
print(sys.version)
#https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype 에 가서
#  JPype1‑1.3.0‑cp39‑cp39‑win_amd64.whl 다운 받고
# C:\Users\user\anaconda3\Lib\site-packages에 저장하고 다음 명령어 실행

os.system('pip install --upgrade pip') #안해도 됨
os.system('pip install JPype1‑1.3.0‑cp39‑cp39‑win_amd64.whl')
os.system('pip install konlpy')
import konlpy
from konlpy.tag import Okt


okt = Okt()  #객체 생성

text = ' 한글 자연어 처리는 재밌다 이제부터 열심히 해야지 ㅎㅎㅎ'

print(okt.morphs(text))

print(okt.morphs(text, stem = True)) #stem기능으로 동사원형 추출

print(okt.nouns(text)) #명사 추출

print(okt.phrases(text)) #어절 단위 추출

print(okt.pos(text)) # 옆에 문법형태도 같이 출력

print(okt.pos(text, join = True))  #리스트로 같이 묶어서 출력









