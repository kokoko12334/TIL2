USE market_db;

-- order by는 해당 열을 기준으로 오름차순으로 정렬
SELECT mem_id, mem_name, debut_date FROM member ORDER BY debut_date;

-- 내림차순
SELECT mem_id, mem_name, debut_date FROM member ORDER BY debut_date DESC;

-- select from where order 순서 지켜야함
SELECT * FROM member WHERE height >= 164 ORDER BY debut_date;

-- 이중 order => 먼저 키순으로 나열하고 그다음 데뷔순으로 정렬(이때 키순으로 나열된 상태에서 그 다음 조건을 실행, 즉 키순이 동률이면 그다음 따지는 것을 말함)
SELECT mem_id, mem_name, debut_date, height FROM member WHERE height >=164 ORDER BY height DESC, debut_date ASC ;



-- limit n번까지 실행 출력
SELECT mem_id, mem_name, debut_date FROM member ORDER BY debut_date LIMIT 3;

SELECT mem_id, mem_name, debut_date FROM member ORDER BY debut_date LIMIT 3,2; -- LIMIT n, m  => n+1포함 m개

-- distinct: 중복제거
SELECT DISTINCT addr FROM member;


-- GROUP BY
-- mem_id 그룹별로 sum(amount)의 결과를 출력해라
SELECT mem_id, SUM(amount) FROM buy GROUP BY mem_id;

SELECT mem_id, SUM(amount*price) FROM buy GROUP BY mem_id;

-- mem_id를 그룹별로 구매갯수의 평균을 구한다. 옆에 ""는 출력의 표현을 바꿈
SELECT mem_id "회원아이디", AVG(amount) "평균구매 갯수" FROM buy GROUP BY mem_id;


-- count(열이름) => 해당 열의 갯수를 세며 *는 그냥 전체 행의 갯수를 센다. 이때 null값은 제외시킨다.
SELECT COUNT(*) FROM member;

SELECT COUNT(phone1) FROM member;


-- having : 그룹함수의 조건절을 처리함.
SELECT mem_id, SUM(price*amount) FROM buy GROUP BY mem_id HAVING SUM(price*amount) >=1000; 

-- 순서: select / from / where / group by / having / order by / limit  순으로 써야함

SELECT mem_id, SUM(price*amount) "total" FROM buy GROUP BY mem_id HAVING SUM(price*amount) >= 1000 ORDER BY SUM(price*amount) DESC;



-- DATE FORMAT
-- DATE_FORMAT(PUBLISHED_DATE,'%Y-%m-%d') 

