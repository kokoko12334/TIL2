DROP TABLE members;


CREATE TABLE members(
	name CHAR(10),
    id VARCHAR(30) PRIMARY KEY,
    passward VARCHAR(15),
    address VARCHAR(30),
    TEL CHAR(9),
    email VARCHAR(20)
	
);


select * from members;

SHOW VARIABLES LIKE 'c%';
SHOW full columns FROM members;
