# API 키를 환경변수로 관리하기 위한 설정 파일
from dotenv import load_dotenv
# API 키 정보 로드
load_dotenv()




from langchain.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

# 화장품 상품의 설명과 메타데이터 생성
docs = [
    Document(
        page_content="수분 가득한 히알루론산 세럼으로 피부 속 깊은 곳까지 수분을 공급합니다.",
        metadata={"year": 2024, "category": "스킨케어", "user_rating": 4.7},
    ),
    Document(
        page_content="24시간 지속되는 매트한 피니시의 파운데이션, 모공을 커버하고 자연스러운 피부 표현이 가능합니다.",
        metadata={"year": 2023, "category": "메이크업", "user_rating": 4.5},
    ),
    Document(
        page_content="식물성 성분으로 만든 저자극 클렌징 오일, 메이크업과 노폐물을 부드럽게 제거합니다.",
        metadata={"year": 2023, "category": "클렌징", "user_rating": 4.8},
    ),
    Document(
        page_content="비타민 C 함유 브라이트닝 크림, 칙칙한 피부톤을 환하게 밝혀줍니다.",
        metadata={"year": 2023, "category": "스킨케어", "user_rating": 4.6},
    ),
    Document(
        page_content="롱래스팅 립스틱, 선명한 발색과 촉촉한 사용감으로 하루종일 편안하게 사용 가능합니다.",
        metadata={"year": 2024, "category": "메이크업", "user_rating": 4.4},
    ),
    Document(
        page_content="자외선 차단 기능이 있는 톤업 선크림, SPF50+/PA++++ 높은 자외선 차단 지수로 피부를 보호합니다.",
        metadata={"year": 2024, "category": "선케어", "user_rating": 4.9},
    ),
]

# 벡터 저장소 생성
vectorstore = Chroma.from_documents(
    docs, OpenAIEmbeddings(model="text-embedding-3-small")
)



from langchain.chains.query_constructor.base import AttributeInfo

# 메타데이터 필드 정보 생성
metadata_field_info = [
    AttributeInfo(
        name="category",
        description="The category of the cosmetic product. One of ['스킨케어', '메이크업', '클렌징', '선케어']",
        type="string",
    ),
    AttributeInfo(
        name="year",
        description="The year the cosmetic product was released",
        type="integer",
    ),
    AttributeInfo(
        name="user_rating",
        description="A user rating for the cosmetic product, ranging from 1 to 5",
        type="float",
    ),
]



from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain_openai import ChatOpenAI

# LLM 정의
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# SelfQueryRetriever 생성
retriever = SelfQueryRetriever.from_llm(
    llm=llm,
    vectorstore=vectorstore,
    document_contents="Brief summary of a cosmetic product",
    metadata_field_info=metadata_field_info,
)


retriever.invoke("평점이 4.8 이상인 제품을 추천해주세요")