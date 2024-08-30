from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

#1. 기본적인 문답 모델지정안하면 'gpt-3.5-turbo-0125' 디폴트
llm = ChatOpenAI(model='gpt-4o-mini')
res = llm.invoke("세상에서 가장 빠른 생물")
print(res)


#2. 체인
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

promt = ChatPromptTemplate.from_template("너는 수학선생이다. 질문:{input}")
str_parser = StrOutputParser()

# 체인 구성 템플릿의 input에 데이터가 들어감.
chain = promt | llm | str_parser
chain.invoke({"input":"x=1, y=2, x+y=?"}) 


#3. 멀티체인
promt1 = ChatPromptTemplate.from_template("너는 주식 전문가야 해당 내용의 전망:{stock}")
promt2 = ChatPromptTemplate.from_template("해당 전망을 평가해라 점수로 {data}:")

chain1 = promt1 | llm | str_parser

promt2 = ChatPromptTemplate.from_template("해당 전망을 평가해라 점수로 {data}:")
chain2 = (
    {"data": chain1}
    | promt2 
    | llm 
    | str_parser
    )

res = chain2.invoke({"stock": "로스웰"})

print(res)


















