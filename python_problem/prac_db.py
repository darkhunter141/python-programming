import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    port = "3306",
    database = "University"
)
mycursor = mydb.cursor()
query = "SELECT \
    student.stu_name AS name,\
    student_attendance.dates AS date \
    FROM student \
    INNER JOIN student_attendance ON student.stu_id = student_attendance.stu_id "
mycursor.execute(query)
#mydb.commit()
#print(mycursor.rowcount, "row is deleted ")
tables = mycursor.fetchall()
for table in tables:
    print(table)