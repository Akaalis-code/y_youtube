![New image of Architecture](./y_nontxt_resources/y_images/y_architechture.png)

<img src="./y_nontxt_resources/y_images/y_old_architech_of_Azdtbrks.png" alt="Old image of Architecture" width="700"/>




# Architecture elements of AZURE DATA BRICKS :
        Contol plane :
        Compute plane :
                Srverless Compute Plane :
                Classic Compute Plane :
        Data plane :



# Unity catalog heirarchy :
        1. Account level : 
                - Each Account (DataBricks or Azure) can contain N number of Workspaces and M number of 
                  metastores(but only one metastore per region)
        2. Metastore :
                - Each metastore can contain N number of catalogs
                - "Hive metastore" , "samples" , "system" , "<your workspace named catalog>" these catalogs come by default
        3. Catalog :
        4. Schema / database :
        5. Tables , Views , functions

When cluster is not started or not attached there is the following behaviour :
        1) Catalog will show tables present in all schemas except hive metastore
        2) DBFS file browser will show "hive metastore tables" but not normal catalog schema tables


# storage areas of DATA bricks elements :

        Notebooks :
        Results displayed in Notebooks :
        Compute resources :
        Workflows :
        Tables :
        

# Checking how different tables behave :
    - Managed tables (Will always maintain data in DELTA LAKE storage)
    - External tables
    - Views
    - Streaming table
    - Delta LIVE table
    - Streaming live table

    - Copy command
    - Autoloader

    - Permissions on objects



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








