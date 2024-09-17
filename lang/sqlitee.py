import sqlite3
import pandas as pd
import MySQLdb

# D 드라이브에 SQLite 데이터베이스 파일 지정
db_path = "D:/financial_reports.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()



# cursor = db.cursor()


# 테이블 생성 SQL
create_table_query = '''
CREATE TABLE IF NOT EXISTS income_statement (
    stock_code VARCHAR(10),
    rcept_no VARCHAR(30),
    bsns_year VARCHAR(10),
    reprt_code VARCHAR(10),
    account_nm VARCHAR(30),
    sj_nm VARCHAR(20),
    thstrm_amount VARCHAR(50),
    currency VARCHAR(10),
    fs_div VARCHAR(10)
)
'''
# 테이블 생성 실행
# cursor.execute(create_table_query)
# db.commit()


create_table_query = '''
CREATE TABLE IF NOT EXISTS balance_sheet (
    stock_code VARCHAR(10),
    rcept_no VARCHAR(30),
    bsns_year VARCHAR(10),
    reprt_code VARCHAR(10),
    account_nm VARCHAR(30),
    sj_nm VARCHAR(20),
    thstrm_amount VARCHAR(50),
    currency VARCHAR(10),
    fs_div VARCHAR(10)
)
'''
# cursor.execute(create_table_query)
# db.commit()

create_table_query = '''
CREATE TABLE IF NOT EXISTS cash_flow (
    stock_code VARCHAR(10),
    rcept_no VARCHAR(30),
    bsns_year VARCHAR(10),
    reprt_code VARCHAR(10),
    account_nm VARCHAR(30),
    sj_nm VARCHAR(20),
    thstrm_amount VARCHAR(50),
    currency VARCHAR(10),
    fs_div VARCHAR(10)
)
'''
# cursor.execute(create_table_query)
# db.commit()


delete_query = """

drop table income_statements

"""



# import pandas as pd
# from sqlalchemy import create_engine

# # 데이터베이스 엔진 생성
# engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@{host}/{db}')

# conn = engine.connect()

# # CSV 파일 경로
# csv_file_path = "C:/Users/KMP/Desktop/재무제표분석고/balance_sheet.csv"
# df = pd.read_csv(csv_file_path, index_col=False, dtype=str)
# df.to_sql('balance_sheet', engine, if_exists='append', index=False)


# # CSV 파일 경로
# csv_file_path = "C:/Users/KMP/Desktop/재무제표분석고/income_statement.csv"
# df = pd.read_csv(csv_file_path, index_col=False, dtype=str)
# df.to_sql('income_statement', engine, if_exists='append', index=False)



# # CSV 파일 경로
# csv_file_path = "C:/Users/KMP/Desktop/재무제표분석고/cash_flow_statement.csv"
# df = pd.read_csv(csv_file_path, index_col=False, dtype=str)
# df.to_sql('cash_flow', engine, if_exists='append', index=False)


# # 커밋 후 연결 종료
# conn.commit()
# conn.close()



