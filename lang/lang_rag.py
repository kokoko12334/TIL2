"""

검색단계: 사용자의 의도를 파악해서 이를 토대로 원하는 문서를 검색
생성단계: 검색된 데이터를 기반으로 LLM모델에 넣어서 답변을 생성

"""

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
load_dotenv()


#1. 파일 추출
file_path = "./[위메프]연결감사보고서(2024.04.09).pdf"
loader = PyPDFLoader(file_path)
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
    query="요즘 경영 위기, 위험한 기업들", 
    k=5)
print(len(docs)) # 결과 내역

docs[0].metadata
for doc in docs:
    print(doc.page_content)

import chromadb

c = chromadb.PersistentClient("D:/chroma")

coll = c.get_collection("dart_test")

docs
coll.get(ids=['0063e947-5b2c-478a-8a24-20fd6f3095a1'], include=['embeddings','metadatas','documents'])
coll.get()

#4 검색(Retieval)

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


template = """
    해당 질문을 문서를 참고하여 정리한 형태로 제공해주세요. 쓸데 없는 말 말고
    객관적인 답변을 위해서 거의 무조건 문서의 내용을 토대로 설명해라
    쓸데없는 말 말고 질문자의 의도에 맞게 어떤 회사와 그 회사가 가진 정보를 토대로만
    설명 위주는 회사를 위주로 해라.
    질문: {question}
    문서: {docs}
    답변예시: ~~의문서를 참고하여 ~~기업이 해당 질문에 적합

"""
prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI(model='gpt-4o-mini', temperature=0)

retriever = vectorstore.as_retriever()
def format_docs(docs):
    arr = []
    for doc in docs:
        source = doc.metadata['source'].split("/")[-1]
        content = doc.page_content
        arr.append(f"{source}: {content}")

    return "\n\n".join(arr)

rag_chain = (
    {"docs": retriever | format_docs, "question": RunnablePassthrough()} # 검색
    | prompt # 생성
    | model
    | StrOutputParser()
)

res = rag_chain.invoke("요즘 뜨는 기업")
print(res)

