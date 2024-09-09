import sqlite3
import pandas as pd

# D 드라이브에 SQLite 데이터베이스 파일 지정
db_path = "D:/financial_reports.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 테이블 생성 SQL
create_table_query = '''
CREATE TABLE IF NOT EXISTS financial_reports (
    name VARCHAR(20),
    code VARCHAR(10),
    rcept_no VARCHAR(30),
    bsns_year INTEGER,
    reprt_code VARCHAR(10),
    account_nm VARCHAR(30),
    sj_nm VARCHAR(20),
    thstrm_amount INTEGER,
    currency VARCHAR(10)
)
'''

delete_query = """

drop table financial_reports

"""


# 테이블 생성 실행
cursor.execute(create_table_query)
# 데이터베이스 저장
conn.commit()

# CSV 파일 경로
csv_file_path = "C:/Users/KMP/Desktop/dart알림기/data/finance.csv"

# CSV 파일을 pandas DataFrame으로 읽기
df = pd.read_csv(csv_file_path)


# DataFrame 데이터를 SQLite에 업로드
df.to_sql('financial_reports', conn, if_exists='append', index=False)

# 커밋 후 연결 종료
conn.commit()
conn.close()



