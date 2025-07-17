import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "library_db"
)

cursor = mydb.cursor()
search_availability = input ( " what do u want : ")
sql = " select * from books WHERE available = %s"
val =  ( int( search_availability),)

cursor.execute( sql , val)
result = cursor.fetchall()

if result:
    for row in result:
         print(f"id :{row[0]} , title  : {row[1]} ,author : {row[2]} , year : {row[3]} , available : {row[4]}")
else:
     print ( "unavailable")

mydb.close()
        
