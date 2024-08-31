from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()
prompt = ChatPromptTemplate.from_messages(

    [
        ("system", "당신은 내 인생의 조언자입니다."),
        MessagesPlaceholder(variable_name="histroy"),
        ("human","{input}")
    ]
)

chain = prompt | llm | StrOutputParser()
