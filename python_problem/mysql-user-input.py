import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost', user='root', password='',port=3306, db='signin')

cur = connection.cursor()
name= input("username: ")
passw= input("passward: ")
#username,password = name,passw
sql = cur.execute('INSERT INTO user(username,password) VALUES ( %s,%s )',(name,passw))
cur.execute("select * from user")
g= cur.fetchall()
for i in g:
    print(i)

connection.commit()
connection.close()
