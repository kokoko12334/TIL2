--  = 혹은 := 를 쓴다 SET에서는 =도 쓸 수 있지만 SELECT는 =를 비교연산자로 인식하기 때문에 =:를 써서 구분한다.
SET @A = (SELECT NAME FROM MEMBER WHERE ID = 1);   
SET @A := (SELECT NAME FROM MEMBER WHERE ID = 1);
SELECT @A:= 3;

-- 별찍기
SET @TEMP:=21; 
SELECT REPEAT('* ', @TEMP:= @TEMP - 1) 
FROM INFORMATION_SCHEMA.TABLES;