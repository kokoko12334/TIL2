#1.프롬프트 템플릿
from langchain_core.prompts import PromptTemplate
template_text = "내 이름은 {name}이고 직업은 {job}입니다."
prompt_template = PromptTemplate.from_template(template_text)
print(prompt_template.format(name="ko",job="dsd"))


#2. 프롬프트 연결
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
combined_template = (
    prompt_template
    + PromptTemplate.from_template("그리고 가족은{familly}입니다.")
    +"\n를 영어로 변역"
)
combined_template.format(name="ko",job="dev",familly="dsadada")

llm = ChatOpenAI(model='gpt-4o-mini')
chain = combined_template | llm | StrOutputParser()
chain.invoke({"name":"ko", "job":{"doctor"}, "familly":{"엄마,형"}})


#3.챗 프롬프트 템플릿 시스템, 유저, 등같은 템플릿
from langchain_core.prompts import ChatPromptTemplate
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 수학선생"),
    ("user", "{user_input}"),
    ("assistant", "1더하기100은 101이다. 잘했어여")
])

messages = chat_prompt.format_messages(user_input="1더하기 100은?")
print(messages)

chain = chat_prompt | llm | StrOutputParser()
chain.invoke({"user_input": "1000+10000은"})


#4. 메시지프롬프트템플릿 위에꺼는 튜플이고 아래꺼는 직접 클래스를 지정
from langchain_core.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate
chat_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template("너는 수학선생"),
        HumanMessagePromptTemplate.from_template("{input}")
    ]
)
chat_prompt.format_messages(input="dsada")





