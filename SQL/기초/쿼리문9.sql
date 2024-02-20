-- sql + 프래그래밍 기능을 스토어드 프로시저를 말함.

USE market_db;

-- 프로시저 생성
DELIMITER $$
CREATE PROCEDURE user_proc()
BEGIN
	SELECT * FROM member;
END $$
DELIMITER ;    

-- 프로시저 호출하기
CALL user_proc();

-- 삭제
DROP PROCEDURE user_proc;



-- 매개변수 포함

DELIMITER $$
CREATE PROCEDURE user_proc1(IN username VARCHAR(10))
BEGIN
	SELECT * FROM member WHERE mem_name = username;
END $$
DELIMITER ;     

CALL user_proc1('에이핑크');


DELIMITER $$
CREATE PROCEDURE user_proc2( IN usernumber INT, IN userheight int)
BEGIN
	SELECT * FROM member WHERE mem_number > usernumber and height > userheight;
END $$
DELIMITER ; 

CALL user_proc2(6, 160);

-- return 값 지정하기

DELIMITER $$
CREATE PROCEDURE user_proc3(
 IN txtvalue CHAR(10),
 OUT outvalue INT)  -- 아웃풋이라고 반환값을 매개변수에 저장
 BEGIN
	INSERT INTO notable VALUES(NULL,txtvalue); -- notable이 당장 없어도 프로시저 생성은 됨 단, 호출할 때 해당 테이블이 없으면 에러 남
	SELECT MAX(id) INTO outvalue FROM notable; -- 과정을 보면 새로운 값을 넣고 난 후에 max(id)값 반환
 END $$
 DELIMITER ;

CREATE TABLE IF NOT EXISTS notable(
	id INT AUTO_INCREMENT PRIMARY KEY,
    txt CHAR(10)
    );

CALL user_proc3('테스트1', @myvalue); -- output의 값을 myvalue에 저장한다는 뜻
SELECT @myvalue;


-- 리턴 연습 2
DELIMITER $$
CREATE PROCEDURE user_proc4(
 IN id CHAR(10),
 OUT outvalue INT)  -- 아웃풋이라고 반환값을 매개변수에 저장
 BEGIN
	SELECT MAX(price) INTO outvalue FROM buy WHERE mem_id = id; 
 END $$
 DELIMITER ;
 
 
 CALL user_proc4('apn', @maxprice);
 SELECT @maxprice ;
 

-- if 절이랑 쓰기


DELIMITER $$
CREATE PROCEDURE ifelse_proc(
	IN memname VARCHAR(10))
BEGIN
	DECLARE debut INT;
    SELECT YEAR(debut_date) into debut FROM member
		WHERE mem_name = memname;
    IF (debut >= 2015)THEN
		SELECT '신인';
	else
		SELECT '고참';
	END IF ; 
END $$
DELIMITER ;     
        

CALL ifelse_proc('소녀시대');

-- 동적 SQL
-- 매개변수로 넣은 테이블의 전체 데이터 출력
DELIMITER $$
CREATE PROCEDURE dynamic_proc(
	IN tablename VARCHAR(20)
    )
BEGIN
	SET @sqlquery = CONCAT('SELECT * FROM', tablename);
    PREPARE myquery FROM @sqlquery;
    EXECUTE myquery;
    DEALLOCATE PREPARE myquery;
END $$
DELIMITER ;

CALL dynamic_proc('member');


