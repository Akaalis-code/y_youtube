
## PARTITIONS vs INDEXING
    To understand this by an analogical example :
        1)  Take a big pile of 1 billion books that you want to arrange in library
        2)  Now the entire library has to be segregated sectionized for better and fast access of any book wanted
        3)  Now each book has { book_id , book_name , book_author , book_genre } 
        4)  If we inspect above attributes of books in library in terms of granularity of distinct data,
            book_genre will have least possible distinct values compared to others followed by
            book_author , book_name , book_id in that increasing order .

    Now if you were to "PARTITION" the library into seperate sections , its meaningless to segregate library based on book_id because of two reasons .
        1) BOOK_ID will be unique and PARTITIONING the library into billion partitions is as good as not doing at all , you have to choose least possible attribute to partition by BOOK_GENRE in this case
        2) The customers of library wont know what they want by BOOK_ID  