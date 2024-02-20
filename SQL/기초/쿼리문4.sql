USE market_db;
-- 내부조인(일반적): 연결된 데이터베이스에서 둘 다 있는 것 회원-구매내역 관계에서는 구매내역에 있는 회원만 출력
 -- 일대다  ->  한쪽에서는 pk이고 다른 쪽에서는 꼭 pk(오직 하나)일 필요는 없다.
 -- 예시로 회원테이블의 id는 pk이지만 구매내역은 여러번 있으므로 id는 여러개가 존재한다. 이때 관계를 기본키(pk)-외래키(fk)관계라고 한다.
 
 
 SELECT * FROM BUY INNER JOIN member ON buy.mem_id = member.mem_id;     -- 앞에 출력 할거 INNER JOIN 연결할거 
SELECT * FROM BUY INNER JOIN member ON buy.mem_id = member.mem_id WHERE buy.mem_id = "GRL";

-- 이떄 on에는 같은 열의 데이터가 같은 것만 즉, mem_id = mem_name 은 동일한 것이 하나도 없기 때문에 아무것도 출력이 안됨.
SELECT buy.mem_id, mem_name, prod_name, addr, CONCAT(phone1, "-", phone2) "연락처" FROM buy INNER JOIN member ON buy.mem_id = member.mem_id;   



-- 외부조인은 내부조인과 달리 한쪽을 기준으로 다 출력 즉 회원테이블을 기준으로 한다면 구매내역이 없는 id도 다 출력 만약 구매내역 기준으로하면 inner 조인과 같음

-- LEFT OUTTER JOIN => JOIN구문 기준으로 왼쪽 기준

SELECT M.mem_id, M.mem_name, B.prod_name, M.addr FROM member M LEFT OUTER JOIN buy B on M.mem_id = B.mem_id ORDER BY M.MEM_ID;   -- member M은 알리아스 즉, 변수명 단축
-- => 출력 결과, mem_id(member)는 다 나옴 구매내역이 없어도 다 나옴

-- right outer join => join기준으로 오른쪽 기준
SELECT M.mem_id, M.mem_name, B.prod_name, M.addr FROM member M RIGHT OUTER JOIN buy B on M.mem_id = B.mem_id ORDER BY M.MEM_ID;
-- => 실행결과는 INNER랑 같고 만약 왼쪽 오른쪽 데이터베이스위치를 바꾸면 위의 LEFT랑 같은 결과 나옴

-- FULL OUTER JOIN => 양쪽 테이블 데이터를 다 포함
-- mysql에서는 full outer를 지원하지 않아서 다음과 같이 union과 같이 써서 표현해야 한다.

SELECT M.mem_id, M.mem_name, B.prod_name, M.addr FROM member M LEFT OUTER JOIN buy B ON M.mem_id = B.mem_id   -- 왼쪽이므로 member의 데이터 값 기준
UNION
SELECT M.mem_id, M.mem_name, B.prod_name, M.addr FROM member M RIGHT OUTER JOIN buy B ON M.mem_id = B.mem_id; -- 오른쪽이므로 buy의 데이터 값 기준



-- 상호조인(cross join): 데이터 하나당 연결된 데이터베이스의 개수만큼 다 출력 즉, member=10개 buy = 12개 이므로 총 120개의 데이터 생성, 별로 의미 없음

SELECT * FROM member CROSS JOIN buy;

-- 다음과 같이 대용량의 데이터를 만들고자 할때 쓰일 수 있음
CREATE TABLE cross_table 
	SELECT * FROM sakila.actor CROSS JOIN world.country;

SELECT * FROM cross_table LIMIT 4;
DROP TABLE CROSS_TABLE;


-- 내부 조인: 한 테이블안에서 관계를 조인 하는 것, 회사의 관계도를 확인할 때 쓰일 수 있음.











