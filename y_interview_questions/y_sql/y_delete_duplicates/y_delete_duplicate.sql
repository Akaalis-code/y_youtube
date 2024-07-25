DISCUSSING POINTS IN THE VIDEO

1) Interview Question
2) Solution
3) Why it shouldnt have worked
4) But why is it working anyway

-------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------


CREATE TABLE tbl_customers_dup_info (name varchar(30) , address varchar(30));




INSERT INTO tbl_customers_dup_info 
values   ('sai' , 'chennai' ),
         ('sai' , 'chennai' ),
         ('sai' , 'chennai' ),
      		('naveen' , 'delhi' ),
      		('hari' , 'kochi' ),
      		('hari' , 'kochi' );


select * from tbl_customers_dup_info;




delete from tbl_customers_dup_info as tgt
where EXISTS (select * from (
                              select *,ROW_NUMBER() over(partition by name,address) as rn
                              from tbl_customers_dup_info as ref
                              where ref.name = tgt.name 
                                and ref.address = tgt.address
                            ) as dt
              where rn>1
              );
              
select * from tbl_customers_dup_info;
