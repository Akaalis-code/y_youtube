CREATE TABLE y_tbl_customers_dup_info (name varchar(30) , address varchar(30), age int);







INSERT INTO y_tbl_customers_dup_info 
values   ('sai' , 'chennai' , 30),
         ('sai' , 'chennai' , 30),
		 ('naveen' , 'delhi' , 20),
		 ('hari' , 'kochi' , 50),
		 ('hari' , 'kochi' , 50);
		
		

		
		
		
		
		
		
		
SELECT * FROM y_tbl_customers_dup_info;














--- My inital thought

--- step 1

SELECT *
FROM y_tbl_cities_dist t1 JOIN y_tbl_cities_dist t2
  on t1.source = t2.destination
 and t1.destination = t2.source
 

--- step 2

SELECT *
FROM y_tbl_cities_dist t1 LEFT JOIN y_tbl_cities_dist t2
  on t1.source = t2.destination
 and t1.destination = t2.source

 
 
--- step 3
 
 SELECT  *,
		case 
			when t1.distance > t2.distance then t1.distance
			else t2.distance
		end as maximum_distance
		
FROM y_tbl_cities_dist t1 LEFT JOIN y_tbl_cities_dist t2
  on t1.source = t2.destination
 and t1.destination = t2.source


--- step 4
 
 SELECT  *,
		case 
			when (t1.distance > t2.distance) or (t2.distance is null) then t1.distance
			else t2.distance
		end as maximum_distance
FROM y_tbl_cities_dist t1 LEFT JOIN y_tbl_cities_dist t2
  on t1.source = t2.destination
 and t1.destination = t2.source
 
 
 
 --- step 5
SELECT t3.* ,
       max(t3.maximum_distance) over(partition by t3.source1 , t3.destination1) as refined_maximum_distance
FROM		
 (
	 SELECT  t1.source as source1,
			 t1.destination as destination1,
			 t1.distance as distance1,
			 t2.source as source2,
			 t2.destination as destinatio2,
			 t2.distance as distance2,
			case 
				when (t1.distance > t2.distance) or (t2.distance is null) then t1.distance
				else t2.distance
			end as maximum_distance
			
	FROM y_tbl_cities_dist t1 LEFT JOIN y_tbl_cities_dist t2
	  on t1.source = t2.destination
	 and t1.destination = t2.source
 ) t3
 
 
 

--- step 6 My Final Solution
SELECT t3.source1 as source ,
	   t3.destination1 as destination,
	   t3.distance1 as distance,
       max(t3.maximum_distance) over(partition by t3.source1 , t3.destination1) as refined_maximum_distance
FROM		
 (
	 SELECT  t1.source as source1,
			 t1.destination as destination1,
			 t1.distance as distance1,
			 t2.source as source2,
			 t2.destination as destinatio2,
			 t2.distance as distance2,
			case 
				when (t1.distance > t2.distance) or (t2.distance is null) then t1.distance
				else t2.distance
			end as maximum_distance
			
	FROM y_tbl_cities_dist t1 LEFT JOIN y_tbl_cities_dist t2
	  on t1.source = t2.destination
	 and t1.destination = t2.source
 ) t3
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
--- My final Solution

SELECT  IF(length(source)>length(destination) , source , destination ) as city1 ,
		IF(length(source)<length(destination) , source , destination ) as city2 ,
		max(distance) as max_distance
FROM y_tbl_cities_dist
group by city1,city2;




















