1 - Create sample data frames  
2 - Show dataframes 
3 - select only few columns
4 - Alias column names
5 - Filter Columns 
6 - Joins of dataframes
7 - Aggregate Functions

from pyspark.sql import SparkSession

ss=SparkSession.builder.getOrCreate()

students_df = ss.createDataFrame( [(1,'harish','A')  , (2,'venkata rama raju','A') , (3,'rajesh','B')]  ,  ('ID','name','section') )
results_df  = ss.createDataFrame( [(1,'physics',94),(2,'maths',95),(1,'maths',90)]  ,  ('ID','subject','marks_scored') )

students_df.show()
results_df.display()



