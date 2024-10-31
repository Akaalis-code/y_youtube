


Q) Find out total sales in a year until that month from begining of the year --->> Rolling Sum 




------- setup  in mysql



-- create
CREATE TABLE tbl_Sales (
  year INTEGER,
  month INTEGER NOT NULL,
  sales INTEGER NOT NULL
);

-- insert
INSERT INTO tbl_sales VALUES (2022, 2, 100);
INSERT INTO tbl_sales VALUES (2022, 3, 700);
INSERT INTO tbl_sales VALUES (2022, 1, 50);
INSERT INTO tbl_sales VALUES (2023, 2, 6000);
INSERT INTO tbl_sales VALUES (2023, 1, 100);
INSERT INTO tbl_sales VALUES (2024, 1, 900);



-- fetch 
SELECT * FROM tbl_sales;



-- Solution 
select * , sum(sales) over (partition by year
                            order by year ASC , month ASC
                            ROWS BETWEEN UNBOUNDED PRECEDING and CURRENT ROW) as rolling_sum
from tbl_sales
order by year ASC ,month ASC;















































----Incomplete------ Below is not a solution but an experimental trail for the above question 
select  * ,
        sales + 
from 
      (
        select  * , ifnull(LAG(sales) over (partition by year order by year DESC , month ASC ) ,sales) as lag_val
        from tbl_sales
      ) as tbl_a
order by year DESC ,month ASC;
