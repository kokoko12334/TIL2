use test;

CREATE TABLE members (
  id INT AUTO_INCREMENT PRIMARY KEY,
  mail VARCHAR(100) NOT NULL,
  name VARCHAR(50) NOT NULL,
  pwd VARCHAR(50) NOT NULL,
  birth DATE NOT NULL,
  phone VARCHAR(20) NOT NULL,
  reg DATE DEFAULT (current_date)
  
);


INSERT INTO members(mail,name,pwd,birth,phone) VALUES("G@mail.com", "ko", "1234", "1996-01-15", "01039391234");

SELECT * FROM members;