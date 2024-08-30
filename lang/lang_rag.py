"""

검색단계: 사용자의 의도를 파악해서 이를 토대로 원하는 문서를 검색
생성단계: 검색된 데이터를 기반으로 LLM모델에 넣어서 답변을 생성

"""

from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
load_dotenv()


#1. 파일 추출
file_path = "C:/Users/KMP/Desktop/dart/company_pre_report/pre_AJ네트웍스-00365387-095570-20240514001237-20230330.txt"
loader = TextLoader(file_path)
file = loader.load()


#2. 파일 청크 생성
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
splites = text_splitter.split_documents(file)

print(len(splites)) # 총 청크된 문서 크기
print(splites[1]) # 하나의 청크
print(splites[1].metadata) # 메타데이터
print(splites[3].page_content)# 내용 

#3. 인덱싱

from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = Chroma.from_documents(
                    persist_directory="D:/chroma",
                    collection_name="dart_test",
                    documents=splites,
                    embedding=embedding_model)


docs = vectorstore.similarity_search(
    query="AJ네트웍스가 판매하는 서비스나 재화 즉, 주요 제품들 나열", 
    k=5)
print(len(docs)) # 결과 내역
for doc in docs:
    print(doc.page_content)


#4 검색(Retieval)

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


template = """
    해당 질문을 문서를 참고하여 정리한 형태로 제공해주세요.
    질문: {question}
    문서: {docs}

"""
prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI(model='gpt-4o-mini', temperature=0)

retriever = vectorstore.as_retriever()
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"docs": retriever | format_docs, "question": RunnablePassthrough()} # 검색
    | prompt # 생성
    | model
    | StrOutputParser()
)

res = rag_chain.invoke("AJ네트웍스가 판매하는 서비스나 재화 즉, 주요 제품들 나열")
print(res)