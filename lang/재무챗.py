from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from dotenv import load_dotenv
from langchain_core.pydantic_v1 import BaseModel, Field
import pandas as pd
import sqlite3

load_dotenv()


df = pd.read_csv("C:/Users/KMP/Desktop/dart알림기/data/company4.csv", index_col=False, dtype=str)

g = {}
for i in range(len(df)):
    code, name = df.iloc[i][['stock_code','corp_name']]
    g[name] = code


with open("./account_nm.txt", "r", encoding="utf-8") as f:
    account_nm = f.read()

query_system_prompt = f"""
CREATE TABLE financial_reports (
    name VARCHAR(20),                -- 회사이름
    code VARCHAR(10),                -- 주식코드
    rcept_no VARCHAR(30),            -- 보고서번호 (14자리 숫자지만, 문자열로 저장)
    bsns_year INTEGER,               -- 사업 연도 (정수형)
    reprt_code VARCHAR(10),          -- 1분기보고서 : 11013 반기보고서 : 11012 3분기보고서 : 11014 사업보고서 : 11011
    account_nm VARCHAR(30),          -- 계정명(예: 자본총계, 유형자산 등등)
    sj_nm VARCHAR(20),               -- 재무상태표, 포괄손익계산서, 현금흐름표,자본변동표
    thstrm_amount REAL,              -- 당기금액 (부동소수점 포함 마이너스 가능)
    currency VARCHAR(10)             -- 통화 단위
);
너는 사용자의 질문에 해당하는 데이터와 관련된 내용만 집중해서 sql쿼리문을 작성할거야. 다시한번
말하지만 집계함수를 쓰는 것이 아니고 사용자의 질문에 해당하는 데이터를 일단 모두 가져오게 하는
쿼리문을 작성하는 거야 질문에 해당하는 내용에서 어떤 데이터가 필요할지 생각하면서 다음의 과정을 진행해라.

 -질문 분석: 사용자의 질문에서 핵심 정보를 파악한다.
 -테이블 및 열 식별: 어떤 테이블에서 데이터를 가져와야 하는지, 어떤 열이 필요한지를 결정한다.
    - name: 어떤기업일지 혹은 복수 개일지
    - bsns_year: 무슨 연도 
    - reprt_code: 1분기, 2분기, 3분기, 4분기 중 어느것을 선택해야할지 혹은 복수 개일지
    - account_nm: 어떠한 재무정보를 가지고 데이터를 가져와야 할지
    
 -조건 정의: 데이터를 필터링할 조건을 파악한다.
 -쿼리 작성: 최종 SQL 쿼리를 작성한다.
 -다시 한번 생각: 최종 SQL 쿼리문이 사용자 질문 의도에 맞는 데이터일지 생각한다.

다시한번 말하지만 최종 검증된 sql쿼리문을 반환해야 한다.
출력은 sql를 키로 하는 json형식으로 해라. 뽑아진 행의 모든 열정보를 가져오는 것이다. 단 코드는 제외해라

다음은 테이블의 열 이름들과 설명이다. 위를 참고하여 사용자의 질문에 데이터를 효과적으로 뽑아낼 수 있는
sqlite 쿼리내용을 작성해라. 만약 insert,update, delete와 같이 불순한 의도를 가지는 질문이면 거절해라


예시 출력은 다음과 같다. 
'sql': 'SELCT * FROM table..'
만약에 예외상황의 질문을 받으면 'sql'대신에 키값을 'no'로 해라

"""

# 원하는 데이터 구조를 정의합니다.
class Topic(BaseModel):
    sql: str = Field(description="sqlquery")
    
parser = JsonOutputParser(pydantic_object=Topic)

llm = ChatOpenAI(model='gpt-4o-mini')

query_prompt = ChatPromptTemplate.from_messages([
    ("system", query_system_prompt),
    ("user", "{user_input}"),
])

chain = query_prompt | llm | parser

user_input = "삼성 전자의 2023년 매출과 영업이익률"
db_result = chain.invoke({"user_input": user_input})

if 'sql' in db_result.keys():
    query = db_result['sql']
else:
    query = db_result['no']

print(query)

db_path = "D:/financial_reports.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
results = cursor.execute(query)

# 결과 가져오기
results = cursor.fetchall()
conn.close()

cols = ('name','rcept_no','bsns_year', 'reprt_code','account_nm','sj_nm','thstrm_amount','currency')
arr = [str(cols)]

for row in results:
    arr.append(str(row))

docs = "\n".join(arr)

print(docs)


prompt = """
CREATE TABLE financial_reports (
    name VARCHAR(20),                -- 회사이름
    code VARCHAR(10),                -- 주식코드
    rcept_no VARCHAR(30),            -- 보고서번호 (14자리 숫자지만, 문자열로 저장)
    bsns_year INTEGER,               -- 사업 연도 (정수형)
    reprt_code VARCHAR(10),          -- 1분기보고서 : 11013 반기보고서 : 11012 3분기보고서 : 11014 사업보고서 : 11011
    account_nm VARCHAR(30),          -- 계정명(예: 자본총계, 유형자산 등등)
    sj_nm VARCHAR(20),               -- 재무상태표, 포괄손익계산서, 현금흐름표,자본변동표
    thstrm_amount REAL,              -- 당기금액 (부동소수점 포함 마이너스 가능)
    currency VARCHAR(10)             -- 통화 단위
);
    데이터베이스의 결과인 docs를 확인하여 사용자의 질문에 대답해라.
    docs: {docs}
"""


prompt = ChatPromptTemplate.from_messages([
    ("system", prompt),
    ("user", "{user_input}"),
])

chain2 = prompt | llm | StrOutputParser()

result = chain2.invoke({"docs":docs,
                        "user_input": user_input})


print(result)

