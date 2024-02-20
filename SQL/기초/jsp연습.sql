
USE myvocab;

CREATE TABLE MEMBERS(
ID NVARCHAR(50),
PWD NVARCHAR(50),
NAME NVARCHAR(50),
GENDER NCHAR(2),
BIRTHDAY CHAR(10),
PHONE CHAR(13),
REGDATE DATE,
EMAIL VARCHAR(200)
);

select * from members where id = "test";

select * from members;

show columns from vocab;


CREATE TABLE vocab(

	ID NVARCHAR(50), foreign key(id) references members(id),
    vocab_name NVARCHAR(50)
);


DELIMITER $$
CREATE PROCEDURE addvocab(IN id_check NVARCHAR(50))
BEGIN
	DECLARE cnt SMALLINT;
    
    SELECT max(vocab_num) INTO cnt FROM vocab WHERE id = id_check ;
    
    IF (cnt IS NULL) THEN
		INSERT INTO vocab VALUES(id_check, 1);
    ELSE
		INSERT INTO vocab VALUES(id_check, cnt + 1);
    END IF;
END $$
DELIMITER ;

CALL addvocab("test2");

select * from vocab;


INSERT INTO vocab VALUES('test5','v3');

delete from vocab where vocab_name ='';



CREATE TABLE words(
	ID NVARCHAR(50), foreign key(id) references members(id),
    vocab_name NVARCHAR(50),
    english VARCHAR(100),
    korean NVARCHAR(50),
    score CHAR(5)  default '0'
);



drop table words;


insert into words(id, vocab_name, english,korean) values('test5', 'v2', 'apple', '사과');

SELECT english, korean, score FROM words WHERE id = 'test5' AND vocab_name = 'v2';

DELETE FROM words WHERE id = 'test5' AND vocab_name = 'v2' AND english = 'peach' AND korean = '복숭아';
select * from words;


DELETE FROM vocab WHERE id = 'test5' AND vocab_name = 'v1';
DELETE FROM words WHERE id = 'test5' AND vocab_name = 'v1';

SELECT * FROM vocab;

select * from words;


UPDATE words SET english = 'banana', korean = '바나나' WHERE id = "test5" AND vocab_name = "토익단어장" AND english = 'apple'; 

