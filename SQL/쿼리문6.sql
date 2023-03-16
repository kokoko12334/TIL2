
CREATE DATABASE naver_db;



CREATE TABLE `naver_db`.`buy` (
  `num` INT NOT NULL AUTO_INCREMENT,
  `mem_id` CHAR(8) NOT NULL,
  `prod_name` CHAR(6) NOT NULL,
  `group_name` CHAR(4) NULL,
  `price` INT UNSIGNED NOT NULL,
  `amount` SMALLINT UNSIGNED NOT NULL,
	PRIMARY KEY (`num`), 
	FOREIGN KEY(mem_id) REFERENCES member(mem_id)      -- 외래키 참조하는 방법 foreign key(만들 테이블 references 테이블명(참조할 열 이름) => buy(다=many) member(일=one) => 일대다 관계로 연결


);
-- 참고로 일대다 관계에서 일(member)에서 pk가 있어야 buy에서 fk에 데이터이름으로 입력 가능 즉, 회원이 되어야 buy항목에 추가될 수 있음.


 
-- 제약조건에 대한 내용
-- primary key: 테이블 당 하나만 지정 가능하며 대표값으로 될 거 같다는 열에다가 지정한다.(이메일, 주민등 구분할 수 있는 데이터 값이 여러개 있다면 이 중에서 하나만 기본키로 지정 할 수 있음)
-- foreign key: 다른 테이블의 pk를 참조함 이때 위에서 언급했듯이 참조한 pk값이 없으면 해당 값은 fk에 생성 할 수 없음 즉, 회원내역에 없는데 구매내역에 나타날 수가 없음 이는 무결성을 보장함.
-- PK-FK 관계에 있다면 일반적인 방법으로 PK는 수정 불가함. 이유는 PK삭제시에 참고하고 있던 FK는 아무것도 아닌 값이 되므로 무결성을 보장하기 위함이다.
-- 이떄에는 외래키를 지정할 때 ON UPDATE CASCADE, ON DELETE CASCADE;를 같이 설정하면 PK변경시 참고하고 있던 FK도 동시에 수정 된다.

-- 나중에 테이블의 기본키 수정시에 
ALTER TABLE member  -- 테이블 이름
	ADD CONSTRAINT PRIMARY KEY(mem_id);   -- 바꿀 열  


-- 나중에 테이블의 fk를 수정 할 시에
ALTER TABLE buy  -- 테이블 이름
	ADD CONSTRAINT  
	FOREIGN KEY(mem_id) REFERENCES member(mem_id);


-- ON UPDATE CASCADE ON DELETE CASCADE

DROP TABLE IF EXISTS buy;

CREATE TABLE buy(
 num INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 mem_id CHAR(8) NOT NULL,
 prod_name CHAR(6) NOT NULL
 );
 
 ALTER TABLE buy    -- 외래 키 지정
	ADD CONSTRAINT
    FOREIGN KEY(mem_id) REFERENCES member(mem_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE;
    
 INSERT INTO member VALUES('BLK', '블랙핑크', 4, '서울', NULL,NULL,NULL,NULL); -- 참조한 PK값이 없으면 FK값 생성 안되므로 MEMBER테이블에 BLK추가
 INSERT INTO buy VALUES(NULL, 'BLK', '지갑');
 INSERT INTO buy VALUES(NULL, 'BLK', '맥북');

UPDATE member SET mem_id = 'PINK' WHERE mem_id = 'BLK';  -- pk값 변경

SELECT M.mem_id, M.mem_name, B.prod_name FROM buy B INNER JOIN member M ON B.mem_id = M.mem_id;


DELETE FROM member WHERE mem_id = 'PINK'; -- pk값 삭제

SELECT * FROM buy; -- fk참조된 값도 같이 삭제



-- 고유키 제약조건(UNIQUE)
-- pk는 null값을 허용안하지만 고유키는 중복x 이지만 null값은 허용함. 그리고 고유키는 여러개 설정 가능함 이는 회원가입시에 이메일 중복에 쓸 수 있음(이메일 입력 안해도 될 때).
-- 테이블 만들 때 UNIQUE 추가 하면 됨.


-- CHECK 제약조건
-- 데이터 값을 넣을 때 데이터의 조건을 설정함.

CREATE TABLE member2(
	mem_id CHAR(8) NOT NULL PRIMARY KEY,
	mem_name VARCHAR(10) NOT NULL,
    height 	TINYINT UNSIGNED NULL CHECK (height >=100), -- height가 100 이상인지 체크
    phone CHAR(3) NULL
);

INSERT INTO member2 VALUES('BLK', '블랙핑크', 99,NULL);  -- 오류남 

-- CHECK 추가 하는 방법 및 IN을 이용한 체크
ALTER TABLE member
	ADD CONSTRAINT
    CHECK (phone IN ('02','031','032','054','055','061')); -- 다음 중 하나가 들어가야 함.
    
    
    
    
--  DEFAULT 제약조건
-- 데이터의 기본 값 설정 (기본 default값은 null임)

CREATE TABLE member3(

	mem_id CHAR(8) NOT NULL PRIMARY KEY,
    mem_name VARCHAR(10) NOT NULL,
    height TINYINT UNSIGNED NULL DEFAULT 160,
    phone CHAR(3) NULL
    );
    
ALTER TABLE member3
		ALTER COLUMN phone SET DEFAULT '02' ;
        
INSERT INTO member3 VALUES('RED','레드벨벳', 161,'054');
INSERT INTO member3 VALUES('SPC', '우주소녀', default, default);        

SELECT * FROM member3;
    
    