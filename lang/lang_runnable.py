from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')
prompt = ChatPromptTemplate.from_template("너는 수학선생이다. 질문:{input}")
str_parser = StrOutputParser()
chain = prompt | llm | str_parser


# 1.RunnablePassthrough 는 runnable 객체이며, runnable 객체는 invoke() 메소드를 사용하여 별도 실행이 가능합니다.
from langchain_core.runnables import RunnablePassthrough

RunnablePassthrough().invoke({"num": 10})
runnable_chain = {"input": RunnablePassthrough()} | prompt | llm

runnable_chain.invoke({"input": "1+2"})


# 2. 다음은 RunnablePassthrough.assign() 을 사용하는 경우와 비교한 결과입니다.

(RunnablePassthrough.assign(new_num=lambda x: x["num"] * 3)).invoke({"num": 1})


## runnable 동시에 실행
from langchain_core.runnables import RunnableParallel

# {country} 의 수도를 물어보는 체인을 생성합니다.
chain1 = (
    PromptTemplate.from_template("{country} 의 수도는 어디야?")
    | llm
    | StrOutputParser()
)

# {country} 의 면적을 물어보는 체인을 생성합니다.
chain2 = (
    PromptTemplate.from_template("{country} 의 면적은 얼마야?")
    | llm
    | StrOutputParser()
)

# 위의 2개 체인을 동시에 생성하는 병렬 실행 체인을 생성합니다.
combined = RunnableParallel(capital=chain1, area=chain2)

combined.invoke({"country": "대한민국"})