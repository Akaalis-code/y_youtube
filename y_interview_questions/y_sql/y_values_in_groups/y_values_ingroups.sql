Discussing points in this VIDEO :
    1) Discuss interview question
    2) Provide my awnser and discuss its inefficiencies
    3) Give Best scalable solution 


CREATE TABLE tbl_a (id int , type varchar(30));




INSERT INTO tbl_a 
values   (1 , 'ball' ),
         (2 , 'ball' ),
         (3 , 'ball' ),
      	 (4 , 'cat'  ),
      	 (5 , 'ball' ),
      	 (6 , 'cat'  ),
      	 (7 , 'ape'  ),
      	 (8 , 'ball' ),
      	 (9 , 'ball' ),
         (10, 'ball' ),
         (11, 'ball' ),
         (12, 'fan'  ),
         (13, 'ball' ),
         (14, 'ball' );

select * from tbl_a;



select count(*)
from (
          select count(set_number) as adjacency
          from (
                      select  *,
                              row_number() over (partition by type)  as rn,
                              id - row_number() over (partition by type) as set_number
                      from tbl_a
                      order by id
                ) as a
          where type = 'ball'
          group by set_number
      ) as c
where adjacency>=2