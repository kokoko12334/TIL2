
-- 트리거: DELETE, INSERT, UPDATE 시행 시 자동으로 다음 과정을 수행하는 것을 말함
-- 데이터 삭제시제(delete)에 해당 데이터를 다시 찾을 수도 있으므로 이를 자동으로 다른 곳에 저장하는 기능에 주로 쓰임
-- update insert delete 문을 실행해야지만 자동으로 시행이 되고 따로 내 마음대로 실행 할 수는 없음.

USE market_db;

DROP TABLE trigger_table;

CREATE TABLE IF NOT EXISTS trigger_table(id INT, txt VARCHAR(10));
INSERT INTO trigger_table VALUES(1, '레드벨벳');
INSERT INTO trigger_table VALUES(2, '잇지');
INSERT INTO trigger_table VALUES(3, '블랙핑크');


DELIMITER $$
CREATE TRIGGER mytigger
	AFTER DELETE -- DELETE이후에 작동하도록 하는 트리거를 설정
    ON trigger_table -- 해당 트리거를 ON 테이블에 부착시킴
    FOR EACH ROW -- 각 행마다 시행시킴(아마도 이거 없으면 한번만 적용되는 듯)
BEGIN
		SET @msg = '가수 그룹이 삭제됨'; -- delete문을 시행하면 trigger도 시행됨으로써 해당 구문을 시행함(확인용)
END $$
DELIMITER ;


DELETE FROM trigger_table WHERE id = 3;

SELECT @msg; -- triger도 시행됨을 확인

SELECT * FROM trigger_table;


-- 트리거를 이용하여 백업테이블 만들기

CREATE TABLE singer (SELECT mem_id, mem_name, mem_number, addr FROM member);

CREATE TABLE backup_singer(
	mem_id CHAR(8) NOT NULL,
    mem_name VARCHAR(10) NOT NULL,
    mem_number INT NOT NULL,
    addr CHAR(2) NOT NULL,
    modtype CHAR(2), -- 변경된 타입(삭제, 수정)
    moddate DATE, -- 변경 날짜
    mouser VARCHAR(30) -- 변경한 사용자
    );

-- UPDATE 트리거
DELIMITER $$
CREATE TRIGGER trigger_singer
	AFTER UPDATE
	ON singer
    FOR EACH ROW
BEGIN
	INSERT INTO backup_singer VALUES(OLD.mem_id, OLD.mem_name, OLD.mem_number, OLD.addr, '수정', CURDATE(), CURRENT_USER() ); -- OLD는 이전의 데이터 값(변경되지 전)을 저장하는 테이블로, SQL에 내장되어 있음.
END $$
DELIMITER ;

-- DELETE 트리거
DELIMITER $$
CREATE TRIGGER trigger_singer2
	AFTER DELETE
	ON singer
    FOR EACH ROW
BEGIN
	INSERT INTO backup_singer VALUES(OLD.mem_id, OLD.mem_name, OLD.mem_number, OLD.addr, '삭제', CURDATE(), CURRENT_USER() ); -- OLD는 이전의 데이터 값(변경되지 전)을 저장하는 테이블로, SQL에 내장되어 있음.
END $$
DELIMITER ;



-- 시행

UPDATE SINGER SET addr = '영국' WHERE mem_id = 'BLK';

DELETE FROM singer WHERE mem_number >= 7;

SELECT * FROM backup_singer;


TRUNCATE TABLE singer; -- 테이블의 내용을 다 삭제

SELECT * FROM singer;
SELECT * FROM backup_singer; -- 확인해보면 백업 테이블에 삭제 전의 내용이 없음. 이는 truncate은 트리거를 작동시키지 않고 오직 update, insert, delete 만으로 시행할 수 있음.









