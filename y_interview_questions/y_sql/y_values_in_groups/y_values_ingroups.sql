-- Q) Write a sql logic to count the number of instances the 
--    word BUS is presnt atleast 3 times in a continuous manner



CREATE TABLE tbl_a (id int , type varchar(30));




INSERT INTO tbl_a 
values   (1 , 'bus' ),
         (2 , 'bus' ),
         (3 , 'bus' ),
      	 (4 , 'car'  ),
      	 (5 , 'car' ),
      	 (6 , 'bus'  ),
      	 (7 , 'air'  ),
      	 (8 , 'bus' ),
      	 (9 , 'bus' ),
         (10, 'bus' ),
         (11, 'bus' ),
         (12, 'ship'  ),
         (13, 'bus' ),
         (14, 'bus' );

select * from tbl_a;



select count(distinct adjacency)
from (
          select  *,
                  count(set_number) over (partition by set_number)as adjacency
          from (
                      select  *,
                              row_number() over (partition by type)  as rn,
                              id - row_number() over (partition by type) as set_number
                      from tbl_a
                      order by id
                ) as a
          where type = 'bus'
      ) as c
where adjacency>=3