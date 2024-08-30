
# LLM, Chat model 2개의 클래스로 관리, LLM은 단일요청, Chatmodel은 대화형히스토리 기억에 적합

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

#1.LLM
llm = ChatOpenAI(model='gpt-4o-mini')
res = llm.invoke("세상에서 가장 빠른 생물")
print(res)

#2.chat model
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

chat = ChatOpenAI()

chat_prompt = ChatPromptTemplate.from_messages(
    [("system", "너는 선생"),
    ("user", "{input}")
])
chain = chat_prompt | chat
chain.invoke({"input": "안녕"})