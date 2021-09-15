import mysql.connector
conn = mysql.mydb = mysql.connector.connect(user='root', password="",port=3306, host= 'localhost',database = 'mysql1st')
#print(conn)
cursor = conn.cursor()
#cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
name = input("enter name: ")
address = input("enter address: ")
sql = cursor.execute("INSERT INTO customers(name,address)VALUES(%s,%s)",(name,address))
sql1 = cursor.execute("SELECT*FROM customers")
myresult = cursor.fetchall()
print(myresult)
for x in myresult:
    print(x)
conn.commit()