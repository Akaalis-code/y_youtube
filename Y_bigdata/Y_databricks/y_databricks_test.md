![Architecture](./y_nontxt_resources/y_images/y_architechture.png)



# Architecture elements of AZURE DATA BRICKS :
        Contol plane :
        Compute plane :
                Srverless Compute Plane :
                Classic Compute Plane :
        Data plane :




# storage areas of DATA bricks elements :

        Notebooks :
        Results displayed in Notebooks :
        Compute resources :
        Workflows :
        Tables :
        

# Checking how different tables behave :
    Managed tables (Will always maintain data in DELTA LAKE storage)
    External tables
    Streaming table
    Delta LIVE table
    Streaming live table

    Managed tables (Will always maintain data in DELTA LAKE storage)
         create or replace table y_most_basic_table 
                as
                (
                        select 'r1c1' as COL1 ,'r1c2' as COL2 ,'r1c3' as COL3
                )
    External tables
    Streaming table
    Delta LIVE table
    Streaming live table








