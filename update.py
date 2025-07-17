import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "library_db"
)

cursor = mydb.cursor()

book_id = input("enter book id to be updated :")
new_status = input("give the availability of book (1 OR ) : ")
sql = (" update books SET  available = %s where id = %s")
val = (int(new_status),int(book_id))

cursor.execute(sql,val)
mydb.commit
cursor.fetchall()

print( cursor.rowcount ,"records updated")

mydb.close()