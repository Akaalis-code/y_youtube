------ MYSQL based syntax , Might require syntax correction in other DB s
-- create
CREATE TABLE table1 (
  col_of_tab1 TEXT
);

CREATE TABLE table2 (
  col_of_tab2 TEXT
);

-- insert
INSERT INTO table1 VALUES ('a'),('a'),('b'),('c'),(NULL) ;
INSERT INTO table2 VALUES ('a'),('b'),('b'),('d'),(NULL),(NULL) ;



select * from table1;
select * from table2;


select * 
from table1 right join 
     table2 on
     ( col_of_tab1 = col_of_tab2 );