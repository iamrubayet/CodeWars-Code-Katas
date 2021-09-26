SELECT 'hello world!' AS "Greeting"



//below another version



CREATE TABLE codewars (
  Greeting varchar(50) NOT NULL
);

INSERT INTO codewars VALUES ('hello world!');
SELECT * FROM codewars WHERE Greeting = 'hello world!';