# Structured streaming :

    Problem statement :-
        While spark sql is there to process BATCH(data size is bound and expected to stay that way) data ,
        There is a need of technology which is capable of working with a "UNBOUND CONTINOUSLY GROWING"
        data sources , in short that kind of data is called STREAMING data.
        That is where STRUCTURED STREAMING comes into picture
    
    How is this different from "SPARK STREAMING" :-
        STRUCTURED STREAMING(Uses dataframe and datasets API s) is advanced version of SPARK STREAMING(Dstream API)
        STRUCTURED STREAMING has been added with many advanced features compared to SPARK STREAMING
        Those details we will see below



# Sources and Sinks

    Sources can be = File source ,Socket Source ,Rate Source ,Rate Per Micro-Batch Source(format:rate-micro-batch) ,Kafka Source

    Sinks are based on the output modes , mentioned as below :

        | SINK TYPE         | OUTPUT MODE              |
        |:-----------------:|:------------------------:|
        | File sink         | Append                   |
        | Memory Sink       | Append, Complete         |
        | KAFKA Sink        | Append, Update, Complete |
        | Console Sink      | Append, Update, Complete |
        | Foreach Sink      | Append, Update, Complete |
        | ForeachBatch Sink | Append, Update, Complete |


# SCHEMA 

    For structured streaming in every tutorial or documentation , info is like SCHEMA needs to be explicitly specified  
    But when I tried , I set config like "spark.sql.streaming.schemaInference = True" and did not give any schema ,  
    it worked fine.

    Example :
        ss.conf.set("spark.sql.streaming.schemaInference", True)
        read_stream_df = ss.readStream.format("csv")\
                        .options(header = True,delimiter = ",", recursiveFileLookup = True )\
                        .load(path)


# STREAMING options or config :

    “maxFilesPerTrigger”


CHECK POINTING
WRITE AHEAD LOGS
WATERMARKING
