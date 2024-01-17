from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:7292@localhost/test1?charset=utf8mb4"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True, pool_size=5, max_overflow=0
)

#add => 
#flush => 데이터베이스에 데이터 옭김 아직 데이터베이스에 반영 아님(db 트랜잭션 buffer에 옮김)
#commit => 데이터베이스에 영구 저장 => flush없이 바로 commmit해도 flush=> commit순으로 자동 flush됨
#rollback => flush 된거 다 삭제(db 트랜잭션 buffer 삭제)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

