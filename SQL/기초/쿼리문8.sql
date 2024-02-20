USE market_db;

-- 클러스터형 인덱스: 영어사전처럼 정렬된 인덱스(pk생성시 자동 생성)  => 정렬된 상태(균형 트리 형태로)를 유지하므로 INSERT 같이 데이터 변화가 있을 시에 성능이 저하 될 수 있음.
-- 보조 인덱스: 책의 맨 뒷 장의 찾아보기 기능(UNIQUE임)

CREATE TABLE table1(
	col1 INT PRIMARY KEY, 
    col2 INT,
    col3 INT
    );

SHOW INDEX FROM table1;
-- key_name이 primary면 클러스터형 인덱스   non_unique 0이면 unique를 의미 =>이중부정


CREATE TABLE table2(
	col1 INT PRIMARY KEY,
    col2 INT unique,
    col3 INT unique
    );
SHOW INDEX FROM table2;
-- KEY_NAME이 자신 열이름이면 보조 인덱스 생성

-- index 지정 
-- 중복 허용되는 인덱스(테이블만들 때 유니크) = 보조 인덱스
CREATE INDEX idx_member_mem_name
 ON member (mem_name);
 
SHOW INDEX FROM member;

-- 중복 허용이 안되는 인덱스(테이블 만들때  pk) = 클러스터 인덱스
CREATE UNIQUE INDEX idx_date
ON member(debut_date);

SHOW INDEX FROM member;


SELECT mem_id FROM member where mem_name = '에이핑크'; -- 실행결과 옆에 execution plan에서 full scan인지 아닌지 확인 가능 full scan 이면 모두 조회, 그 외에는 인덱스를 쓴다고 보면 됨

-- 이때 인덱스를 지정해도 mysql이 인덱스로 찾는게 빠른지, full이 빠른지 판단해서 시행해서 인덱스는 지정해도 full scan을 할 때도 있음.

