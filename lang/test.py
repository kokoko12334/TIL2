from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
load_dotenv()
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from tqdm import tqdm
# 지정된 디렉토리 경로

directory = r"C:/Users/KMP/Desktop/dart/company_pre_report"
files = []
for filename in os.listdir(directory):
    files.append(directory+"/"+filename)

embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

for file_path in tqdm(files[:10]):
    #1. 파일 추출
    loader = TextLoader(file_path)
    file = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    splites = text_splitter.split_documents(file)

    from langchain.vectorstores import Chroma
    from langchain_openai import OpenAIEmbeddings

    embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
    db = Chroma.from_documents(persist_directory="D:/chroma",
                        collection_name="dart_test2",
                        embedding=embedding_model,
                        documents=splites,
    )



docs = db.similarity_search(
    query="요즘뜨는 기업", 
    k=5)

docs
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





