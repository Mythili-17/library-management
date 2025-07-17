import mysql.connector
mydb = mysql.connector.connect(

    host = "localhost",
    user = "root",
    password = "root",
    database = "library_db"
)

cursor = mydb.cursor()

sql ="INSERT into books ( title , author , year, available) VALUES (%s ,%s,%s, %s)"
val = ("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, True)

cursor.execute(sql,val)
mydb.commit
print(sql)
print(val)

print(cursor.rowcount ,"record inserted.")

cursor.execute("select * from books")
result = cursor.fetchall()

for row in result :
    print(f"id :{row[0]} , title  : {row[1]} ,author : {row[2]} , year : {row[3]} , available : {row[4]}")




mydb.close
