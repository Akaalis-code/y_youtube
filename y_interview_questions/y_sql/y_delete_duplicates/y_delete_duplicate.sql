DISCUSSING POINTS IN THE VIDEO

1) Interview Question (Delete duplicates)
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



-------------------------------------------------------------------------------------------------------


CREATE TABLE tbl_customers_dup_info (name varchar(30) , address varchar(30) , dummy_column varchar(30));




INSERT INTO tbl_customers_dup_info 
values   ('sai' , 'chennai' ,'a'),
         ('sai' , 'chennai' ,'b'),
         ('sai' , 'chennai' ,'c'),
      		('naveen' , 'delhi' ,'d'),
      		('hari' , 'kochi' ,'e'),
      		('hari' , 'kochi' ,'f');


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