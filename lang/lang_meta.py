from typing import Literal, List, Optional
from pydantic import BaseModel, Field
from langchain import hub
from langchain_community.document_transformers.openai_functions import (
    create_metadata_tagger,
)
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
load_dotenv()

#https://teddylee777.github.io/langchain/metadata-tagger/
# PDF 파일 열기

file_path ="[위메프]연결감사보고서(2024.04.09).pdf"
loader = PyPDFLoader(file_path)
data = loader.load()

# 추출할 속성의 내용을 정의
class Properties(BaseModel):
    # 키워드
    keyword: List[str] = Field(
        description="several keywords extracted from review")
    # 요약문
    summarize: Optional[List[str]] = Field(
        description="Summarize the content of the original text in 30"
    )

# metadata 태거를 생성합니다.
document_transformer = create_metadata_tagger(
    Properties,  # 추출할 속성
    ChatOpenAI(temperature=0, model="gpt-4o-mini"),  # OpenAI 모델
)

# 프롬프트를 불러옵니다.
prompt =  ChatPromptTemplate.from_messages([
    ("system", 
"You need to write keywords and a summary for the given file. The summary should be written in 10 sentences or less."),
    ("user", "{user_input}"),
])


enhanced_documents = document_transformer.transform_documents(
    data, prompt=prompt)


enhanced_documents
