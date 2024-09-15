import sqlite3
import pandas as pd

# D 드라이브에 SQLite 데이터베이스 파일 지정
db_path = "D:/financial_reports.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 테이블 생성 SQL
create_table_query = '''
CREATE TABLE IF NOT EXISTS income_statement (
    stock_code VARCHAR(10),
    rcept_no VARCHAR(30),
    bsns_year INTEGER,
    reprt_code VARCHAR(10),
    account_nm VARCHAR(30),
    sj_nm VARCHAR(20),
    thstrm_amount INTEGER,
    currency VARCHAR(10),
    fs_div VARCHAR(10)
)
'''
# 테이블 생성 실행
cursor.execute(create_table_query)
conn.commit()


create_table_query = '''
CREATE TABLE IF NOT EXISTS balance_sheet (
    stock_code VARCHAR(10),
    rcept_no VARCHAR(30),
    bsns_year INTEGER,
    reprt_code VARCHAR(10),
    account_nm VARCHAR(30),
    sj_nm VARCHAR(20),
    thstrm_amount INTEGER,
    currency VARCHAR(10),
    fs_div VARCHAR(10)
)
'''
cursor.execute(create_table_query)
conn.commit()

create_table_query = '''
CREATE TABLE IF NOT EXISTS cash_flow (
    stock_code VARCHAR(10),
    rcept_no VARCHAR(30),
    bsns_year INTEGER,
    reprt_code VARCHAR(10),
    account_nm VARCHAR(30),
    sj_nm VARCHAR(20),
    thstrm_amount INTEGER,
    currency VARCHAR(10),
    fs_div VARCHAR(10)
)
'''
cursor.execute(create_table_query)
conn.commit()


delete_query = """

drop table income_statements

"""


# 테이블 생성 실행
cursor.execute(create_table_query)
# 데이터베이스 저장
conn.commit()

# CSV 파일 경로
csv_file_path = "C:/Users/KMP/Desktop/재무제표시발/balance_sheet.csv"
df = pd.read_csv(csv_file_path, index_col=False, dtype=str)
df.to_sql('balance_sheet', conn, if_exists='append', index=False)

# CSV 파일 경로
csv_file_path = "C:/Users/KMP/Desktop/재무제표시발/income_statement.csv"
df = pd.read_csv(csv_file_path, index_col=False, dtype=str)
df.to_sql('income_statement', conn, if_exists='append', index=False)


# CSV 파일 경로
csv_file_path = "C:/Users/KMP/Desktop/재무제표시발/cash_flow_statement.csv"
df = pd.read_csv(csv_file_path, index_col=False, dtype=str)
df.to_sql('cash_flow', conn, if_exists='append', index=False)


# 커밋 후 연결 종료
conn.commit()
conn.close()



