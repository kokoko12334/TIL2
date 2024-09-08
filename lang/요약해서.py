from dotenv import load_dotenv
from langchain_community.document_loaders import JSONLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

load_dotenv()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

file_path = "./report_file.json"

loader = JSONLoader(file_path, jq_schema='.messages[].content', text_content=True) 
docs = loader.load()
splites = text_splitter.split_documents(docs)

docs[0].page_content
docs

#3. 인덱싱
import chromadb
from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
persistent_client = chromadb.PersistentClient("D:/chroma")
collection = persistent_client.get_or_create_collection("dart_report2")

vector_store2 = Chroma(
    client=persistent_client,
    collection_name="dart_report2",
    embedding_function=embedding_model,
)

vector_store2.add_documents(docs)

docs = vector_store2.similarity_search(
    query="요즘 경영 위기, 위험한 기업들", 
    k=5)

print(len(docs)) # 결과 내역

docs[0].metadata
for doc in docs:
    print(doc.page_content)


#4 검색(Retieval)

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


template = """

    유저의 질문을 해당 문서를 참고해서 정리해서 제공해라
    질문: {question}
    참고 문서: {docs}

"""
prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI(model='gpt-4o-mini', temperature=0)

retriever2 = vector_store2.as_retriever()
def format_docs(docs):
    arr = []
    for doc in docs:
        source = doc.metadata['source'].split("/")[-1]
        content = doc.page_content
        arr.append(f"{source}: {content}")

    return "\n\n".join(arr)

rag_chain2 = (
    {"docs": retriever2 | format_docs, "question": RunnablePassthrough()} # 검색
    | prompt # 생성
    | model
    | StrOutputParser()
)

res = rag_chain2.invoke("CSA코스믹의 주요상품,제품")
print(res)

