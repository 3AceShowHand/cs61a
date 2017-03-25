.read data.sql

-- Q2
CREATE TABLE obedience as
  -- REPLACE THIS LINE
  SELECT seven, denero FROM students;


-- Q3
CREATE TABLE blue_dog as
  -- REPLACE THIS LINE
  SELECT color, pet FROM students where color = 'blue' and pet = 'dog';


-- Q4
CREATE TABLE smallest_int as
  -- REPLACE THIS LINE
  SELECT time, smallest From students where smallest > 6 ORDER BY smallest LIMIT 20;


-- Q5
CREATE TABLE sevens as
  -- REPLACE THIS LINE
  SELECT s.seven FROM students as s, checkboxes as c WHERE s.number = 7 and c.'7' = 'True' and s.time = c.time;


-- Q6
CREATE TABLE matchmaker as
  -- REPLACE THIS LINE
  SELECT first.pet, first.song, first.color, second.color FROM students as first, students as second
    WHERE first.time < second.time and first.pet = second.pet and first.song = second.song;


