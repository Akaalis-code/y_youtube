// pip install pyspark 

from pyspark.sql import SparkSession

ss=SparkSession.builder.getOrCreate()

students_df = ss.createDataFrame( [(1,'rama','A') , (2,'raju','A') , (1,'rama','B')]  ,  ('ID','name','section') )
results_df  = ss.createDataFrame( [(1,'physics',94),(2,'maths',95),(1,'maths',90)]  ,  ('ID','subject','marks_scored') )

students_df.show()
results_df.display()



