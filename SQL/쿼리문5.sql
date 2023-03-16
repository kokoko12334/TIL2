
USE market_db;


-- procedure(함수 같은거)

DELIMITER $$
CREATE PROCEDURE ifproc1()   -- procedure(함수) 만들기
BEGIN     
	IF 100 = 100 THEN
		SELECT '100은 100과 같습니다.';
	END IF;
    
END $$
DELIMITER ;

CALL ifproc1(); -- 함수 불러오기



DELIMITER $$

CREATE PROCEDURE ifproc2()
BEGIN
	DECLARE mynum INT; -- 변수선언
    SET mynum = 200;
    IF mynum = 100 THEN
		SELECT '100입니다.';
    ELSE    
		SELECT '100이 아닙니다.';
    END IF;
END $$
DELIMITER ;   -- ;는 띄어 쓰어야함.
   
CALL ifproc2();


DELIMITER $$
CREATE PROCEDURE ifproc3()
BEGIN
	DECLARE debutdate DATE;
    DECLARE curdate DATE;
    DECLARE days INT;
    
    SELECT debut_date INTO debutDate FROM market_db.member WHERE mem_id = 'APN' ; -- member테이블의 debut_date 열의 값(mem_id = apn)을 선언한 변수인 debutdate에 넣어라
    
    SET curdate = CURRENT_DATE();  -- 현재 날짜
    SET days = DATEDIFF(curdate, debutdate);   -- 현재날짜 - 데뷔날짜
    
    IF (days/365) >= 5 THEN
		SELECT CONCAT('데뷔한지', days, '일이 지났습니다.');
    ELSE
		SELECT '데뷔한지' + days + '일밖에 안되었네요.';
    END IF;
END $$
DELIMITER ;

CALL ifproc3();    


-- case문



DELIMITER $$
CREATE PROCEDURE caseproc()
BEGIN
	DECLARE point INT;
    DECLARE credit CHAR(1);
    SET point = 8;
    
    CASE
		WHEN point >= 90 THEN
			SET credit = 'A';
        WHEN point >= 80 THEN
			SET credit = 'B';
        WHEN point >= 70 THEN
			SET credit = 'C';
        WHEN point >= 60 THEN
			SET credit = 'D';
        ELSE
			SET credit = 'F';
        END CASE;
        SELECT CONCAT('취득점수: ', point), CONCAT('학점: ', credit);
 END $$
 DELIMITER ;
 
 CALL caseproc();


-- case문 응용

SELECT M.mem_id, M.mem_name, SUM(price*amount) '총 구매액',
		CASE
			WHEN (SUM(price*amount) >= 1500) THEN '최우수고객'
			WHEN (SUM(price*amount) >= 1000) THEN '우수고객'
			WHEN (SUM(price*amount) >= 1) THEN '일반고객'
			ELSE '유령고객'
		END '회원등급'  -- CASE문 출력결과의 열 이름
    FROM buy B
		RIGHT OUTER JOIN member M
        ON B.mem_id = M.mem_id
	GROUP BY M.mem_id
    ORDER BY SUM(price*amount) DESC;
    

-- while
DROP PROCEDURE IF EXISTS whileproc;

DELIMITER $$
CREATE PROCEDURE whileproc()
BEGIN
	DECLARE i INT;
	DECLARE total INT;
    SET i = 1;
    SET total = 0;
	
    WHILE (i <= 100) DO
		SET total = total +i;
        SET i = i + 1;
    END WHILE;
    
    SELECT '1부터 100까지의 합: ', total;
 END $$
 DELIMITER ;
 CALL whileproc();


-- while 응용

DELIMITER $$
CREATE PROCEDURE whileproc2()
BEGIN
	DECLARE i INT;
	DECLARE total INT;
    SET i = 1;
    SET total = 0;
	
    mywhile:
    WHILE (i <= 100) DO -- WHILE문의 라벨
		IF (i%4 = 0) THEN
			SET i = i + 1;
            ITERATE mywhile; -- if문에 걸리면 while 라벨로 돌아가
        END IF;
        
		SET total = total +i;
        
        IF(total > 1000) THEN   
			LEAVE mywhile; -- total이 1000 넘으면 그냥 while문 나감(break)
        END IF;
        
        SET i = i + 1;
    END WHILE;
    
    SELECT '1부터 100까지의 합(4의 배수 제외, 합 1000초과 시 종료: ', total;
 END $$
 DELIMITER ;
 CALL whileproc2();
 
 
 
 
 -- prepare execute 쿼리문3 에서도 언급  이를 동적 sql 즉, 고정된 명령문이 아닌 변수가 포함된 쿼리문을 말함.
 
 
 CREATE TABLE gate_table (
	id INT AUTO_INCREMENT PRIMARY KEY,
    entry_time DATETIME
    );
    
 SET @curdate = CURRENT_TIMESTAMP();
 
 PREPARE myquery FROM 'INSERT INTO gate_table VALUES(NULL,?)';
 EXECUTE myquery USING @curdate;
 DEALLOCATE PREPARE myquery; -- 함수 실행하고 닫아주는 것
 
 SELECT * FROM gate_table
    
    
    
    
 
 
 
 
 
