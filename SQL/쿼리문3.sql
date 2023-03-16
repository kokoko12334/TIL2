USE market_db;


CREATE TABLE market_db.hongong1 (
	toy_id INT,
    toy_name CHAR(4),
    age INT
    );

INSERT INTO hongong1 VALUES(1,"우디", 25);

-- 제외시킬 열이 있을 경우에
INSERT INTO hongon1(toy_id, toy_name) VALUES(2, "버즈");

-- auto_increment => 숫자 자동 증가 이떄 primary key를 지정 해주어야 함.
CREATE TABLE hongong2(
toy_id INT AUTO_INCREMENT PRIMARY KEY,
toy_name CHAR(4),
age INT
);

-- AUTO INCREMENT를 다음과 값이 순서를 뒤죽박죽으로 쓰면 자동으로 순서를 맞추어줌 이때 자동 1 증가는 마지막 행의 번호를 기준으로 함.
INSERT INTO hongong2 VALUES(NULL, "보핍", "5");
INSERT INTO hongong2 VALUES(5, "슬링키", 3);
INSERT INTO hongong2 VALUES(NULL, "슬링", 3);
INSERT INTO hongong2 VALUES(4, "슬키", 3);
INSERT INTO hongong2 VALUES(NULL, "키", 3);
SELECT * FROM hongong2;

-- 어디 까지 입력되었는지 확인
SELECT LAST_INSERT_ID();

-- 증가폭 바꾸기
ALTER TABLE hongong2 AUTO_INCREMENT = 100;
INSERT INTO hongong2 VALUES(NULL, "ㅇㅇㅇ인", 11);



-- INSERT INTO (행이름) SELECT: 다른 DB의 정보를 가져올 때 
SELECT COUNT(*) FROM world.city;

-- city의 열정보
DESC world.city;


CREATE TABLE city_popul (
	city_name CHAR(35),
    population INT
    );

INSERT INTO city_popul SELECT name, population FROM world.city;
SELECT * FROM city_popul;



-- update: 데이터 수정    set은 바꿀 구문 where은 어디를 바꿀것인지

UPDATE city_popul SET city_name = "서울" WHERE city_name = "Seoul";
SELECT * FROM city_popul WHERE city_name = "서울";


UPDATE city_popul SET city_name = "뉴욕", population = 0 WHERE city_name = "New york";
SELECT * FROM city_popul WHERE city_name = "뉴욕";

-- WHERE절이 없는 경우에는 모든 데이터가 변경사항을 따른다. 다음과 같이 단위를 바꾸고자 할 때 where없이 쓰일 수는 있다.
UPDATE city_popul SET population = population/10000;
SELECT * FROM city_popul LIMIT 5;



-- delete
DELETE FROM city_popul WHERE city_name LIKE "New%";
-- 삭제 갯수를 지정하고 싶을 때
DELETE FROM city_popul WHERE city_name LIKE "New%" LIMIT 5;




-- 데이터 타입

-- tinyint : 1바이트     smallint: 2바이트   int: 4바이트  bigint: 8바이트

-- char(n): n공간을 차치함 만약 char(10)이고 3글자만 저장하면 => 7공간 낭비     varchar(n): 연결리스트처럼 유기적으로 함 즉, varchar(10)=> 3공간만 쓰면 일단 3공간만 할당 이때 새로 공간을 생성하는 연산을 하기때문에 속도는 char가 빠름(조금더) 
-- 그리고 varchar가 char보다 최대공간이 높음
-- longtext: 더 긴 문자를 저장  ,         longblob: 큰 바이너리코드 저장 


-- float: 실수형(4바이트)   double: 실수형(8바이트)

-- date: yyyy--mm--dd의 형식으로 날짜표현(3바이트)         time: hh-mm 형식으로 시간 표현(3바이트)   datetime: yyyy-mm-dd hh mm 형식으로, 날짜, 시간을 표현(8바이트)

-- 변수 선언방법: SET @변수이름 = 변수의 값    출력은 SELECT @변수이름
SET @x = 5;
SET @Y = 10;
SELECT @X;
SELECT @X+@Y;


-- PREPARE EXECUTE   : 함수를 지정하고 변수를 너어서 시행하는 것과 같음.
SET @count = 3;

PREPARE mysql FROM "SELECT mem_name, height FROM member ORDER BY height LIMIT ?"; -- prepare로 함수 같은거 지정
EXECUTE mysql USING @count;  -- excute 이름  using 변수를 이용하여 시행



-- 형변환
-- 명시적: (cast 바꿀대상 as 바꿀데이터타입)       ,      (convert  바꿀대상, 바꿀데이터타입)
SELECT CAST(AVG(price) AS SIGNED) FROM buy; -- signed는 정수형 변환 unsigned는 음수값을 제거 이때 제거된 음수값의 데이터표현범위를 양수에 몰아줌 즉 -10~+10범위의 표현을 0~+20으로 변환
SELECT CONVERT(AVG(price), SIGNED) FROM buy;

-- 출력문으로 활용 (concat(문자열1, 문자열2) 은 두 개의 문자열을 합침)

SELECT num, CONCAT(CAST(price AS CHAR), "X", CAST(amount AS CHAR), "=") "가격*수량", price*amount "구매액" FROM buy;


-- 암시적: 알아서 형변환 수행

SELECT ("100" + "200") "RESULT" ;  -- 알아서 정수형으로 시행
SELECT CONCAT(100, 200); -- CONCAT은 문자열만 가능하므로 알아서 문자열로 변환
SELECT 16 > "15sD3D"; -- 앞에 있는 연속된 숫자만 정수로 변환  즉, 앞의 15만 정수로 변환 되서 16>15임.
SELECT 1 > "DSADAD"; -- 문자열은 0으로 처리




