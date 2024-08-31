from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()
prompt = ChatPromptTemplate.from_messages(

    [
        ("system", "당신은 내 인생의 조언자입니다. 내 고민에 대한 상담을 해주세요."),
        # 이전의 대화기록을 메모리에 저장 즉 프롬프트에 해당 내역을 프롬프트에 저장
        MessagesPlaceholder(variable_name="history"), 
        ("human","{input}")
    ]
)

runnable = prompt | llm | StrOutputParser()


#1. 인메모리방식(서버의 메모리에 저장)
# 일단 서버리스 특성상 계정없이 하려면 세션id 웹브라우저저장소를 활용

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

store = dict()

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]    


# input은 사용자의 입력, history는 메시지 키값즉 인메모리 키값 -> get_session_history의 데이터를 -> history에 매핑
with_message_history = (
    RunnableWithMessageHistory(
        runnable=runnable,
        get_session_history=get_session_history,
        input_messages_key="input",
        history_messages_key="history"
    )
)

session_id = "kmp"
res = with_message_history.invoke(
    {"input": "나의 미래에 대한 걱정"},
    config={"configurable": {"session_id": session_id}}
)
print(res)

# session_id를 기준으로 인메모리에 저장된것을 참고한 것을 볼 수 있음.
res2 = with_message_history.invoke(
    {"input": "해당 내용을 영어로 번역해봐"},
    config={"configurable": {"session_id": session_id}}
)
print(res2)

##상세하게 sesssion id 구분하기 config 부분을 커스터마이징하여 사용가능
from langchain_core.runnables import ConfigurableFieldSpec

store = dict()

def get_session_history(user_id: str, conversation_id: str) -> BaseChatMessageHistory:
    if (user_id, conversation_id) not in store:
        store[(user_id, conversation_id)] = ChatMessageHistory()
    return store[(user_id, conversation_id)] 

with_message_history = (
    RunnableWithMessageHistory(
        runnable=runnable,
        get_session_history=get_session_history,
        input_messages_key="input",
        history_messages_key="history",
        history_factory_config=[
            ConfigurableFieldSpec(
                id="user_id",
                annotation=str,
                name="UserID",
                description="유저의 고유식별자",
                default="",
                is_shared=False
            ),
            ConfigurableFieldSpec(
                id="conversation_id",
                annotation=str,
                name="CONID",
                description="유저별 채팅식별자",
                default="",
                is_shared=False
            )
        ]
    )
)

user_id = "kmp"
conversation_id = "2"
res = with_message_history.invoke(
    {"input": "나의 미래에 대한 걱정"},
    config={"configurable": {"user_id": user_id, "conversation_id": conversation_id}}
)
print(res)

res2 = with_message_history.invoke(
    {"input": "해당 내용을 영어로 번역"},
    config={"configurable": {"user_id": user_id, "conversation_id": conversation_id}}
)
print(res2)
