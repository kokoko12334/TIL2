--  USE: 퀴리를 사용할 데이터베이스를 선택한다. 
-- 선택된 db는 진한 글씨가 됨.
USE market_db    ;

-- select 열이름 from 테이블이름
SELECT * FROM member;

-- 해당 db와 다른 db를 참조하고싶으면(use사용없이) 다음과 같이 사용됨
SELECT * FROM shop_db.member;

-- 뒤에 where 열이름 = 조건
SELECT * FROM member WHERE mem_name = "블랙핑크";
SELECT * FROM member WHERE height >= 160 AND mem_number >= 4;

-- between: 정수형에서 사이 표현
SELECT * FROM member WHERE height >= 163 AND height <= 165;
SELECT * FROM member WHERE height BETWEEN 163 AND 165;

-- in 해당 값이 포함된 거 확인
SELECT * FROM member WHERE addr = "경기" OR addr = "전남" OR addr = "경남";
SELECT * FROM member WHERE addr IN("경기", "전남", "경남");

-- like %는 나머지 글자 전체   _는 나머지 글자 한개 __는 나머지 글자 두개
SELECT * FROM member WHERE mem_name LIKE "우%";
SELECT * FROM member WHERE mem_name LIKE "우___";

-- 원하는 열들만 확인
SELECT mem_id, mem_name FROM member;







 