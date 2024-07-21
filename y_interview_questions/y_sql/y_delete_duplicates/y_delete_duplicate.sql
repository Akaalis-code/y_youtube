
CREATE TABLE y_tbl_customers_dup_info (name varchar(30) , address varchar(30), age int);




INSERT INTO y_tbl_customers_dup_info 
values   ('sai' , 'chennai' , 30),
         ('sai' , 'chennai' , 30),
		('naveen' , 'delhi' , 20),
		('hari' , 'kochi' , 50),
		('hari' , 'kochi' , 50);


select * from y_tbl_customers_dup_info;


delete from y_tbl_customers_dup_info as tgt
where EXISTS (select * from (
                              select *,ROW_NUMBER() over(partition by name,address,age) as rn
                              from y_tbl_customers_dup_info as ref
                              where ref.name = tgt.name 
                                and ref.address = tgt.address
                                and ref.age = tgt.age
                            ) as dt
              where rn>1
              );
              
select * from y_tbl_customers_dup_info;