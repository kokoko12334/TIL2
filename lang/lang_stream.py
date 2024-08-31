from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')
promt = ChatPromptTemplate.from_template("너는 수학선생이다. 질문:{input}")
str_parser = StrOutputParser()

chain = promt | llm | str_parser


# stream
for token in chain.stream({"input":"x=1, y=2, x+y=?"}):
    print(token, end="", flush=True)

# async stream
async def stream():
    # 비동기 스트림을 사용하여 'YouTube' 토픽의 메시지를 처리합니다.
    async for token in chain.astream({"input":"x=1, y=2, x+y=?"}):
        # 메시지 내용을 출력합니다. 줄바꿈 없이 바로 출력하고 버퍼를 비웁니다.
        print(token, end="", flush=True)

# async invoke
my_process = chain.ainvoke({"topic": "NVDA"})

