from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_community.document_loaders import PyPDFLoader
from tqdm import tqdm

load_dotenv()

file = "CSA 코스믹 20240814004024 반기보고서 (2024.06) 20240814.pdf"
path = 'D:/dart/report/' + file

def get_docs(file_path):

    loader = PyPDFLoader(file_path) 
    docs_lazy = loader.lazy_load()
    docs = []
    if "감사보고서" in file_path:
        for _ in range(6):
            next(docs_lazy)

        for doc in docs_lazy:
            doc.page_content = file + doc.page_content
            docs.append(doc)

    else:

        for _ in range(4):
            next(docs_lazy)

        while True:
            doc = next(docs_lazy)
            if "사업의 내용" in doc.page_content:
                doc.page_content = file + doc.page_content
                docs.append(doc)
                break
        for doc in docs_lazy:
            if "이사회 등 회사의 기관에 관한 사항" in doc.page_content:
                break
            doc.page_content = file + doc.page_content
            docs.append(doc)

    return docs


# 사용 예제
directory_path = 'D:/dart/report'
if os.path.exists(directory_path):
    files = os.listdir(directory_path)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
files
pdfs = []
for file in tqdm(files[:100]):
    file_path = f"{directory_path}/{file}"
    docs = get_docs(file_path)
    splites = text_splitter.split_documents(docs)
    pdfs.append(splites)

#3. 인덱싱
import chromadb
from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
persistent_client = chromadb.PersistentClient("D:/chroma")
collection = persistent_client.get_or_create_collection("dart_report")

vector_store = Chroma(
    client=persistent_client,
    collection_name="dart_report",
    embedding_function=embedding_model,
)

for docs in pdfs:
    vector_store.add_documents(docs)

docs = vector_store.similarity_search(
    query="CSA 코스믹의 최근 매출액과 매출액에서 가장 높은 비중을 갔고 있는 상품들", 
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

    유저의 질문을 해당 문서를 참고해서 정리해서 제공해라 그리고 출처도 밝혀라 
    질문: {question}
    참고 문서: {docs}

"""
prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI(model='gpt-4o-mini', temperature=0)


template_intend = """
    다음 질문의 의도랑 키워드를 파악한다. 질문의 의도는 간결하고 명확하게 재구성하고
    키워드는 핵심적으로 파악 
    질문:{input}
    '질문의도': ""
    '키워드': []

"""
prompt2 = ChatPromptTemplate.from_template(template_intend)


retriever = vector_store.as_retriever(k=10)

def format_docs(docs):
    arr = []
    for doc in docs:
        source = doc.metadata['source'].split("/")[-1]
        content = doc.page_content
        arr.append(f"{source}: {content}")

    return "\n\n".join(arr)

rag_chain = (
    
    {"docs": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)


chain1 = prompt2 | model | StrOutputParser() | retriever | format_docs

rag_chain2 = (
    {"docs": chain1, "question": RunnablePassthrough()}    
    | prompt
    | model
    | StrOutputParser()
)
rag_chain2
res = rag_chain2.invoke("AJ네트윅스 주요제품과 매출비중")
print(res)

