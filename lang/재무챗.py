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

print(g)

with open("./account_nm.txt", "r", encoding="utf-8") as f:
    account_nm = f.read()

query_system_prompt = f"""

CREATE 재무상태표, 손익계산서, 현금흐름표 테이블 공통 (
    stock_code VARCHAR(10) -- 주식코드
    rcept_no VARCHAR(30) -- 보고서번호 (14자리 숫자지만, 문자열로 저장)
    bsns_year INTEGER -- 사업 연도 (정수형)
    reprt_code VARCHAR(10) -- 1분기보고서 : 11013 반기보고서 : 11012 3분기보고서 : 11014 사업보고서 : 11011
    thstrm_amount INTEGER -- 당기금액 (부동소수점 포함 마이너스 가능)
    currency VARCHAR(10) -- 통화 단위
    fs_div VARCHAR(10) -- 개별/연결구분 OFS:재무제표, CFS:연결재무제표
)

각 테이블에 대한 정보인데 너가 추려야할 열이름만 언급한 것이다.

1. 재무상태표(balance_sheet)
재무상태표는 일정시점의 재무상태를 나타내는 표입니다.
​기업의 기본적인 사업자금인 자산, 빌려온 자금인 부채, 경영자나 투자자가 투자한 금액인 자본.

유동자산
비유동자산
자산총계
유동부채
비유동부채
부채총계
자본
자본총계

2. 손익계산서(income_statement)
손익계산서는 일정기간동안의 재무성과를 나타내는 표입니다.
기업의 수익과 비용에 관련된 정보를 나타냅니다..

매출
영업이익
기타수익
기타비용
판매비와관리비
분기총포괄손익
지배기업소유주지분
비지배지분
매출원가
기본주당순이익
금융원가
금융수익
매출총이익
법인세비용
기타포괄손익

3. 현금흐름표(cash_flow)
현금흐름표는 일정기간동안 기업의 현금흐름을 나타내는 표입니다.
영업활동, 투자활동, 재무활동에 사용된 현금의 정보를 나타냅니다. 

영업활동현금흐름
투자활동현금흐름
재무활동현금흐름
기초현금및현금성자산
기말현금및현금성자산



너는 사용자의 질문에 해당하는 데이터와 관련된 내용만 집중해서 sql쿼리문을 작성할거야. 다시한번
말하지만 집계함수를 쓰는 것이 아니고 사용자의 질문에 해당하는 데이터를 일단 모두 가져오게 하는
쿼리문을 작성하는 거야 질문에 해당하는 내용에서 어떤 데이터가 필요할지 생각하면서 다음의 과정을 진행해라.
이때 account_nm은 명칭은 다 달라서 특정 짓기 힘들다 따라서 정의할 열은 다음의 4개 밖에 없고
SELECT * FROM 처럼 모든 열을 가져오도록 해라 너가 할 것은 조건만 파악하는 것이다.

 -질문 분석: 사용자의 질문에서 핵심 정보를 파악한다.
 -테이블 및 열 식별: 어떤 테이블에서 데이터를 가져와야 하는지, 어떤 열이 필요한지를 결정한다. 기업은 무조건 종목코드로 찾아라
    - table: cash_flow, balance_sheet, income_statement
    - code: 기업의 주식 종목 코드(예: KX하이텍의 종목코드는 052900)
    - bsns_year: 무슨 연도 
    - reprt_code: 1분기(11013), 2분기(11012), 3분기(11014), 4분기(11011) 중 어느것을 선택해야할지 혹은 여러개일지
    
 -조건 정의: 데이터를 필터링할 조건을 파악한다.
 -쿼리 작성: 최종 SQL 쿼리를 작성한다.
 -다시 한번 생각: 최종 SQL 쿼리문이 사용자 질문 의도에 맞는 데이터일지 생각한다.

다시한번 말하지만 최종 검증된 sql쿼리문을 반환해야 한다.
출력은 sql를 키로 하는 json형식으로 해라. 뽑아진 행의 모든 열정보를 가져오는 것이다.

다음은 테이블의 열 이름들과 설명이다. 
위를 참고하여 사용자의 질문에 데이터를 효과적으로 뽑아낼 수 있는
sqlite 쿼리내용을 작성해라 테이블끼리 join이 필요하면 하고 여러개의 쿼리문이 있다면 리스트로 담아서 보내라
무조건 하나여도 리스트로 담아서 보내라 
만약 drop, update, delete같은 요구나 재무관련 질문이 아니면 거부하고
answer은 빈 배열인 []를 내고 error에 키값으로 하는 메시지 출력

예시 출력은 다음과 같다.
answer: ['SELCT * FROM table..']
error : ''
무조건 키값은 answer, error 제발 시발년아
"""

# 원하는 데이터 구조를 정의합니다.
class Topic(BaseModel):
    answer: str = Field(description="outputformat")
    
parser = JsonOutputParser(pydantic_object=Topic)

llm = ChatOpenAI(model='gpt-4o-mini')

query_prompt = ChatPromptTemplate.from_messages([
    ("system", query_system_prompt),
    ("user", "{user_input}"),
])

company = "골드앤에스"
code = g[company]

chain = query_prompt | llm | parser

user_input = f"{code}해당 기업의 총 부채와 자본 대비 부채 비율은 어떤가요? 2024년"
db_result = chain.invoke({"user_input": user_input})

query = db_result['answer']
print(db_result)
print(query)

db_path = "D:/financial_reports.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()


cols = ('stock_code', 'rcept_no','bsns_year', 'reprt_code','account_nm','sj_nm','thstrm_amount','currency',"fs_div")
arr = [str(cols)]
for q in query:
    results = cursor.execute(q)
    results = cursor.fetchall()
    for row in results:
        arr.append(str(row))
docs = "\n".join(arr)
conn.close()
print(docs)

prompt = """

    stock_code: 주식코드
    rcept_no: 보고서번호 (14자리 숫자지만, 문자열로 저장)
    bsns_year: 사업 연도 (정수형)
    reprt_code: 1분기보고서 : 11013 반기보고서 : 11012 3분기보고서 : 11014 사업보고서 : 11011
    account_nm: 계정명(예: 자본총계, 유형자산 등등)
    sj_nm : 재무상태표, 손익계산서, 현금흐름표
    thstrm_amount: 당기금액
    currency: 통화 단위
    fs-div: 개별/연결구분	OFS:재무제표, CFS:연결재무제표
    너는 재무 분석가이다. 전문가스러운 분석을 수행해라.

    데이터베이스의 결과인 docs를 확인하여 사용자의 질문에 대답해라. 
    또한 참고 데이터의 신뢰를 위해 보고서 번호도 마지막에 정리해라
    docs: {docs}
"""


prompt = ChatPromptTemplate.from_messages([
    ("system", prompt),
    ("user", "{user_input}"),
])

llm = ChatOpenAI(model='gpt-4o-mini')
chain2 = prompt | llm | StrOutputParser()

result = chain2.invoke({"docs":docs,
                        "user_input": user_input})


print(result)

