

-- 스토어드 함수: sum()처럼 함수를 직접 만듬 프로시저랑 차이점은 프로시저는 쿼리에 대한 흐름을 말하고 함수는 말 그대로 count, sum처럼 계산하는 식을 말하는 것 같음


SET GLOBAL log_bin_trust_function_creators = 1; -- 함수 사용시에 다음과 같은 설정을 한번 시행한다. 한번 시행하면 그다음부터는 할 필요없음

USE market_db;

DELIMITER $$
CREATE FUNCTION sumfunc(number1 INT, number2 INT)
	RETURNS INT
BEGIN
	RETURN number1 + number2;
END $$
DELIMITER ;     

SELECT sumfunc(1,2); -- 해당 함수를 호출할 떄는 select로 출력




-- 커서(기본개념)

-- 테이블의 한 행씩 거쳐가는 것을 말함 즉, 데이터를 한행, 한행 씩 실행해가면서 설정한 구역까지 실행함.

-- 커서를 이용해서 멤버수의 평균 값 구하기

DROP PROCEDURE cursor_proc;
DELIMITER $$
CREATE PROCEDURE cursor_proc()
BEGIN

-- 설정해야 할 것들
DECLARE memnumber INT; -- 각 행의 멤버 인원수
DECLARE cnt INT DEFAULT 0; -- 멤버 수(커서가 내려가면서 +1씩)
DECLARE total INT DEFAULT 0; -- 각 행의 멤버 인원수의 누적 합
DECLARE endrow BOOLEAN DEFAULT FALSE ;  -- 끝나는 지점(마지막행)

DECLARE cursor1 CURSOR FOR -- 커서 설정으로, mem_number에 대한 연산 시작을 알림
	SELECT mem_number FROM member;
    
DECLARE CONTINUE HANDLER-- for not found는 더 이상 행이 없을 때 endrow = True로 해줌으로써 반복문의 종료 조건을 설정
	FOR NOT FOUND SET endrow = TRUE;
    
-- 커서 열기
OPEN cursor1;

-- 행 반복하기
cursor_loop: LOOP

	FETCH cursor1 INTO memnumber;  -- 커서를 한 행의 결과값을 저장할 변수에 연결
    
    IF endrow THEN   -- 루프를 빠져나갈 조건
		LEAVE cursor_loop;
    END IF;
    
    SET cnt = cnt + 1;
    SET total = total + memnumber;
END LOOP cursor_loop;

SELECT(total/cnt) AS '회원의 평균 인원수';

CLOSE cursor1;
END $$
DELIMITER ; 


CALL cursor_proc();












