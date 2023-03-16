
-- view: 가상의 테이블, 바로가기 아이콘처엄 실제 테이블에 연결
-- 뷰를 쓰는 이유: 예민한 정보는 숨길 수 있으므로 보안에 도움이 됨.
-- 원본 테이블에는 접근을 제한하고 뷰에만 접근해서 보안을 강화함.
-- 그리고 복잡한 쿼리로 짠 결과물을 view에 저장함으로 써 다음에도 쿼리를 다시 짜지 않고 해당 결과를 불러 올 수 있음.
-- 뷰에서만 primary key를 확인 할 수 없음.
-- 기존 테이블이 삭제되면 해당 테이블을 참고하고 있던 뷰는 더 이상 조회가 안됨.
USE market_db;
 
-- 뷰 생성
CREATE VIEW v_member
AS SELECT mem_id, mem_name FROM member;   -- as이하 구문에서 mem_id, mem_name을 가진 테이블을 view가 가짐.


-- 그냥 해당 명령문을 실행함. 다음과 같은 방법으로 실행
SELECT * FROM v_member2;




-- 바뀐 열 이름에 띄어쓰기가 있으면 1 왼쪽에 있는 `(백틱)으로 조회해야 한다.
CREATE VIEW v_test
AS
	SELECT B.mem_id 'Member ID', M.mem_name AS 'Member Name', B.prod_name "Product Name"
    FROM buy B
    INNER JOIN member m ON B.mem_id = M.mem_id;
    
SELECT DISTINCT `Member ID`, `Member Name` FROM v_test;    
    
describe v_test; -- 정보 조회
drop view v_test; -- 삭제



-- create or replace : 기존 뷰가 있으면 덮어씀.
CREATE OR REPLACE VIEW v_test
AS
	SELECT B.mem_id 'Member ID', M.mem_name AS 'Member Name', B.prod_name "Product Name"
    FROM buy B
    INNER JOIN member m ON B.mem_id = M.mem_id;


show create view v_test;  -- view의 원래 구문 조회






