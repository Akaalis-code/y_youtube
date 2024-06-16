CREATE TABLE y_tbl_cities_dist (source varchar(30) , destination varchar(30), distance int);







INSERT INTO y_tbl_cities_dist 
values   ('bangalore' , 'chennai' , 300),
		 ('chennai' , 'bangalore' , 400),
		 ('bangalore' , 'delhi' , 2000),
		 ('delhi' , 'bangalore' , 2500),
		 ('bangalore' , 'kochi' , 500),
		 ('bangalore' , 'kochi' , 400);
		
		

		
		
		
		
		
		
		
SELECT * FROM y_tbl_cities_dist;















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
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 
 
 
 
 
--- My Friends Solution

SELECT  IF(length(source)>length(destination) , source , destination ) as city1 ,
		IF(length(source)<length(destination) , source , destination ) as city2 ,
		max(distance) as max_distance
FROM y_tbl_cities_dist
group by city1,city2;





















--- BEST and final solution
select  t3.source,
		t3.destination,
		t3.distance,
		max(t3.distance) over (partition by t3.city1 , t3.city2) as maximum_distance
FROM		
(
	SELECT  source,
			destination,
			IF(length(source)>length(destination) , source , destination ) as city1 ,
			IF(length(source)<length(destination) , source , destination ) as city2 ,
			distance
	FROM y_tbl_cities_dist
) t3;



